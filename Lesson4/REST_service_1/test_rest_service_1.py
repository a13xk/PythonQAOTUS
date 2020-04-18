import pytest


class TestDogAPI:
    """
    Sample tests for Dog API https://dog.ceo/dog-api/
    """

    def test_list_all_breeds(self, api_client):
        """
        /breeds/list/all - List all breed names including sub breeds.
        """
        endpoint = "/breeds/list/all"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()

        # Check status
        assert res_json.get("status") == "success"

        # Check type of 'message' key
        assert isinstance(res_json.get("message"), dict)

    #

    def test_single_random_image(self, api_client):
        """
        /breeds/image/random - Random image from any breed.
        """
        endpoint = "/breeds/image/random"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()

        # Check status
        assert res_json.get("status") == "success"

        # Check type of 'message' key and URL naming
        message = res_json.get("message")
        assert isinstance(message, str)
        assert message.startswith("https://images.dog.ceo/breeds/")
        assert message.endswith(".jpg")
    #

    @pytest.mark.parametrize(
        argnames="number",
        argvalues=[-1, 0, 1, 2, 33, 49, 50, 999],
        ids=[
            "Negative number",
            "Zero",
            "One",
            "Two",
            "1 < x <50",
            "49",
            "Fifty",
            "More than 50"
        ])
    def test_multiple_random_images(self, api_client, number):
        """
        /breeds/image/random/<n> - Get <n> random images from any breed (max. 50)
        """
        endpoint = f"/breeds/image/random/{str(number)}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()

        # Check status
        assert res_json.get("status") == "success"

        # Check length of 'message' list
        message = res_json.get("message")
        assert isinstance(message, list)
        if number < 2:
            assert len(message) == 1, f"Incorrect length of 'messages' list. Expected 1, got {len(message)}"
        elif 2 <= number <= 50:
            assert len(message) == number, f"Incorrect length of 'messages' list. Expected {number}, got {len(message)}"
        elif number > 50:
            assert len(message) == 50, f"Incorrect length of 'messages' list. Expected 50, got {len(message)}"
        else:
            assert False

        # Check URL naming in 'message' list
        for i in message:
            i = i.lower()
            assert i.startswith("https://images.dog.ceo/breeds/")
            assert i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".txt")
    #

    @pytest.mark.parametrize(argnames="breed", argvalues=[
        "affenpinscher",
        "dane",
        "greyhound",
        "hound"
    ])
    def test_all_images_by_breed(self, api_client, breed):
        """
        /breed/{breed}/images - Get all breed images.
        """
        endpoint = f"/breed/{breed}/images"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()

        # Check status
        assert res_json.get("status") == "success"

        # Check type of 'message' key
        message = res_json.get("message")
        assert isinstance(message, list)

        # Check URL naming in 'message' list
        for i in message:
            i = i.lower()
            assert i.startswith("https://images.dog.ceo/breeds/")
            assert i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".txt")
    #

    @pytest.mark.parametrize(
        argnames="breeds",
        argvalues=[
            ("terrier", True, True),
            ("borzoi", True, False),
            ("zzzz", False, False)
        ],
        ids=[
            "Breed with sub-breeds",
            "Breed without sub-breeds",
            "Non-existing breed"
        ]
    )
    def test_list_all_sub_breeds(self, api_client, breeds):
        """
        /breed/{breed}/list - List sub breeds.
        """
        breed, exists, has_sub_breeds = breeds
        endpoint = f"/breed/{breed}/list"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()

        # Check status
        if exists:
            assert res_json.get("status") == "success"

            # Check type of 'message' key
            message = res_json.get("message")
            assert isinstance(message, list)

            if has_sub_breeds:
                assert len(message) > 0, f"Incorrect length of 'messages' list. Expected > 0, got {len(message)}"
            else:
                assert len(message) == 0, f"Incorrect length of 'messages' list. Expected 0, got {len(message)}"

        else:
            assert res_json.get("status") == "error"
    #
#
