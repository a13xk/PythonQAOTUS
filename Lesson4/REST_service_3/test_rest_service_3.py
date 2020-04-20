from jsonschema import validate
import pytest


class TestJSONPlaceholder:
    """
    Sample tests for JSONPlaceholder API https://jsonplaceholder.typicode.com
    """
    @pytest.mark.parametrize(
        argnames="resource_name",
        argvalues=[
            "posts",
            "comments",
            "albums",
            "photos",
            "todos",
            "users"
        ],
        ids=[
            "/posts - 100 posts",
            "/comments - 500 comments",
            "/albums - 100 albums",
            "/photos - 5000 photos",
            "/todos - 200 todos",
            "/users - 10 users"
        ]
    )
    def test_list_all_resources(self, api_client, resource_name):
        """
        GET https://jsonplaceholder.typicode.com/{resource_name} - List all resources
        """
        endpoint = f"/{resource_name}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        # Check object type
        res_json = res.json()
        assert isinstance(res_json, list)

        # Check schema
        if resource_name == "posts":
            assert len(res_json) == 100
            schema = {
                "type": "object",
                "properties": {
                    "userId": {"type": "number"},
                    "id": {"type": "number"},
                    "title": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["userId", "id", "title", "body"]
            }
        elif resource_name == "comments":
            assert len(res_json) == 500
            schema = {
                "type": "object",
                "properties": {
                    "postId": {"type": "number"},
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["postId", "id", "name", "email", "body"]
            }
        elif resource_name == "albums":
            assert len(res_json) == 100
            schema = {
                "type": "object",
                "properties": {
                    "userId": {"type": "number"},
                    "id": {"type": "number"},
                    "title": {"type": "string"}
                },
                "required": ["userId", "id", "title"]
            }
        elif resource_name == "photos":
            assert len(res_json) == 5000
            schema = {
                "type": "object",
                "properties": {
                    "albumId": {"type": "number"},
                    "id": {"type": "number"},
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "thumbnailUrl": {"type": "string"}
                },
                "required": ["albumId", "id", "title", "url", "thumbnailUrl"]
            }
        elif resource_name == "todos":
            assert len(res_json) == 200
            schema = {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "userId": {"type": "number"},
                    "title": {"type": "string"},
                    "completed": {"type": "boolean"}
                },
                "required": ["id", "userId", "title", "completed"]
            }
        elif resource_name == "users":
            assert len(res_json) == 10
            schema = {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "username": {"type": "string"},
                    "email": {"type": "string"},
                    "address": {
                        "type": "object",
                        "properties": {
                            "street": {"type": "string"},
                            "suite": {"type": "string"},
                            "city": {"type": "string"},
                            "zip-code": {"type": "string"},
                            "geo": {
                                "type": "object",
                                "properties": {
                                    "lat": {"type": "string"},
                                    "lng": {"type": "string"}
                                }
                            },
                        }
                    },
                    "phone": {"type": "string"},
                    "website": {"type": "string"},
                    "company": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "catchPhrase": {"type": "string"},
                            "bs": {"type": "string"}
                        }
                    }
                },
                "required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
            }
        else:
            assert False

        for elem in res_json:
            validate(instance=elem, schema=schema)
    #

    @pytest.mark.parametrize(
        argnames="post_id",
        argvalues=[-1, 0, 1, 33, 100, 101],
        ids=[
            "Negative",
            "Zero",
            "1 <= id <= 100 (min)",
            "1 <= id <= 100",
            "1 <= id <= 100 (max)",
            "id > 100",
        ]
    )
    def test_get_post(self, api_client, post_id):
        """
        GET https://jsonplaceholder.typicode.com/posts/{post_id} - Get post
        """
        endpoint = f"/posts/{str(post_id)}"
        res = api_client.get(path=endpoint)

        # Check status code
        if 1 <= post_id <= 100:
            assert res.status_code == 200

            # Check object type
            res_json = res.json()
            assert isinstance(res_json, dict)

            # Check object schema
            schema = {
                "type": "object",
                "properties": {
                    "userId": {"type": "number"},
                    "id": {"type": "number"},
                    "title": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["userId", "id", "title", "body"]
            }
            validate(instance=res_json, schema=schema)
        else:
            assert res.status_code == 404
    #

    @pytest.mark.parametrize(
        argnames="input_id, output_id",
        argvalues=[
            (-1, -1),
            (0, 0),
            (1, 1),
            (10000, 10000)
        ],
        ids=[
            "Invalid: Negative",
            "Invalid: Zero",
            "Valid: 1",
            "Valid; 10000"
        ]
    )
    @pytest.mark.parametrize(
        argnames="input_title, output_title",
        argvalues=[
            ("My Title", "My Title"),
            ("", ""),
            (100, 100),
            ("&", "&")
        ]
    )
    def test_create_post(self, api_client, input_id, output_id, input_title, output_title):
        """
        POST https://jsonplaceholder.typicode.com/posts/ - Create post
        """
        endpoint = "/posts"
        create_data = {
            "title": input_title,
            "body": "some body",
            "userId": input_id
        }
        res = api_client.post(path=endpoint, data=create_data)
        res_json = res.json()
        assert res_json.get("title") == str(output_title)
        assert res_json.get("body") == "some body"
        assert res_json.get("userId") == str(output_id)
    #

    @pytest.mark.parametrize(
        argnames="post_id",
        argvalues=[-1, 0, 1, 33, 100, 101],
        ids=[
            "Invalid post ID: Negative",
            "Invalid post ID: Zero",
            "Valid post ID: 1",
            "Valid post ID: 1 < id < 100",
            "Valid post ID: 100 (max)",
            "Invalid post ID: > 100",
        ]
    )
    def test_update_post(self, api_client, post_id):
        """
        PUT https://jsonplaceholder.typicode.com/posts/{post_id} - Update post
        """
        endpoint = f"/posts/{str(post_id)}"
        update_data = {
            "userId": 1,
            "id": post_id,
            "title": "New title",
            "body": "New body"
        }
        res = api_client.put(path=endpoint, data=update_data)
        if 0 < post_id <= 100:
            assert res.status_code == 200
            res_json = res.json()
            assert res_json.get("userId") == "1"
            assert res_json.get("id") == post_id
            assert res_json.get("title") == "New title"
            assert res_json.get("body") == "New body"
        else:
            assert res.status_code == 500
    #

    @pytest.mark.parametrize(
        argnames="post_id",
        argvalues=[-1, 0, 1, 33, 100, 101],
        ids=[
            "Invalid post ID: Negative",
            "Invalid post ID: Zero",
            "Valid post ID: 1",
            "Valid post ID: 1 < id < 100",
            "Valid post ID: 100 (max)",
            "Invalid post ID: > 100",
        ]
    )
    def test_delete_post(self, api_client, post_id):
        """
        DELETE https://jsonplaceholder.typicode.com/posts/{post_id} - Delete post
        """
        endpoint = f"/posts/{str(post_id)}"
        res = api_client.delete(path=endpoint)
        assert res.status_code == 200
    #
#
