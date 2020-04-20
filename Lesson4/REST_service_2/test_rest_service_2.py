import cerberus
import pytest


class TestOpenBreweryDB:
    """
    Sample tests for Open Brewery DB API https://www.openbrewerydb.org/
    """

    @pytest.mark.parametrize(
        argnames="brewery_name",
        argvalues=[
            "cooper",
            "brewing_co",
            "modern%20times"
        ],
        ids=[
            "Brewery name: single word",
            "Brewery name: underscores",
            "Brewery name: URL encodings"
        ]
    )
    def test_list_breweries_by_name(self, api_client, brewery_name):
        """
        by_name - Filter breweries by name.

        Note: For the parameters, you can use underscores or url encoding for spaces.
        """
        endpoint = f"?by_name={brewery_name}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()
        assert isinstance(res_json, list)

        for brewery in res_json:
            schema = {
                "id": {"type": "number", 'required': True},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string", "nullable": True},
                "latitude": {"type": "string", "nullable": True},
                "phone": {"type": "string"},
                "website_url": {"type": "string", "nullable": True},
                "updated_at": {"type": "string"},
                "tag_list": {"type": "list"}
            }
            v = cerberus.Validator()
            assert v.validate(brewery, schema), f"Error in brewery:\n {brewery}"

            if "_" in brewery_name:
                brewery_name = brewery_name.replace("_", " ")
            if "%20" in brewery_name:
                brewery_name = brewery_name.replace("%20", " ")
            assert brewery_name in brewery.get("name").lower()
    #

    @pytest.mark.parametrize(
        argnames="state_t",
        argvalues=[
            ("ohio", "Ohio"),
            ("new_york", "New York"),
            ("new%20mexico", "New Mexico")
        ],
        ids=[
            "State name: single word",
            "State name: underscores",
            "State name: URL encodings"
        ]
    )
    def test_list_breweries_by_state(self, api_client, state_t):
        """
        by_state - Filter breweries by state.

        Note: Full state name is required; no abbreviations.
        For the parameters, you can use underscores or url encoding for spaces.
        """
        state_name, state_full_name = state_t
        endpoint = f"?by_state={state_name}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()
        assert isinstance(res_json, list)

        for brewery in res_json:
            schema = {
                "id": {"type": "number", 'required': True},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string", "allowed": [state_full_name]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string", "nullable": True},
                "latitude": {"type": "string", "nullable": True},
                "phone": {"type": "string"},
                "website_url": {"type": "string", "nullable": True},
                "updated_at": {"type": "string"},
                "tag_list": {"type": "list"}
            }
            v = cerberus.Validator()
            assert v.validate(brewery, schema), f"Error in brewery:\n {brewery}"
    #

    @pytest.mark.parametrize(
        argnames="brewery_type",
        argvalues=[
            "micro", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor"
        ]
    )
    def test_list_breweries_by_type(self, api_client, brewery_type):
        """
        Filter by type of brewery.

        Must be one of: micro, regional, brewpub, large, planning, bar, contract, proprietor
        """
        endpoint = f"?by_type={brewery_type}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()
        assert isinstance(res_json, list)

        for brewery in res_json:
            schema = {
                "id": {"type": "number", 'required': True},
                "name": {"type": "string"},
                "brewery_type": {"type": "string", "allowed": [brewery_type]},
                "street": {"type": "string"},
                "city": {"type": "string", "nullable": True},
                "state": {"type": "string", "nullable": True},
                "postal_code": {"type": "string", "nullable": True},
                "country": {"type": "string"},
                "longitude": {"type": "string", "nullable": True},
                "latitude": {"type": "string", "nullable": True},
                "phone": {"type": "string"},
                "website_url": {"type": "string", "nullable": True},
                "updated_at": {"type": "string"},
                "tag_list": {"type": "list"}
            }
            v = cerberus.Validator()
            assert v.validate(brewery, schema), f"Error in brewery:\n {brewery}"
    #

    @pytest.mark.parametrize(
        argnames="breweries_count",
        argvalues=[-1, 0, None, 1, 20, 50, 999],
        ids=[
            "Negative (same as default)",
            "Zero (none)",
            "None (no value)",
            "One",
            "Twenty (default)",
            "Maximum (50)",
            "Above maximum (same as maximum)"
        ]
    )
    def test_list_breweries_per_page(self, api_client, breweries_count):
        """
        per_page - Number of breweries to return each call.

        Note: Default per page is 20. Max per page is 50.
        """

        endpoint = f"?per_page={str(breweries_count)}"
        res = api_client.get(path=endpoint)

        # Check status code
        assert res.status_code == 200

        res_json = res.json()
        assert isinstance(res_json, list)

        if breweries_count is None:
            assert len(res_json) == 20, \
                f"With no value for breweries count, 20 breweries per page are expected, got {len(res_json)}"
        elif breweries_count < 0:
            assert len(res_json) == 20, \
                f"With negative breweries count, 20 breweries per page are expected, got {len(res_json)}"
        elif breweries_count == 0:
            assert len(res_json) == 0, \
                f"With zero breweries count empty list is expected, got {len(res_json)}"
        elif 0 < breweries_count < 50:
            assert len(res_json) == breweries_count, \
                f"With positive breweries count up to 50, {str(breweries_count)} per page are expected, got {len(res_json)}"
        elif breweries_count == 50:
            assert len(res_json) == 50, \
                f"With 50 breweries count (maximum allowed value), 50 breweries per page are expected, got {len(res_json)}"
        elif breweries_count > 50:
            assert len(res_json) == 50, \
                f"With more than 50 breweries count (maximum allowed value), 50 breweries per page are expected, got {len(res_json)}"
    #

    @pytest.mark.parametrize(
        argnames="brewery_id",
        argvalues=[-1, 0, 1, 555, 8029, 8030, 10000, "", "abc"],
        ids=[
            "Negative",
            "Zero",
            "1 <= id <= 8029 ",
            "1 <= id <= 8029 ",
            "1 <= id <= 8029 ",
            "id > 8029 ",
            "id > 8029 ",
            "Empty string",
            "Arbitrary string"
        ]
    )
    def test_get_brewery(self, api_client, brewery_id):
        """
        id - Get a single brewery.
        """
        endpoint = f"/{str(brewery_id)}"
        res = api_client.get(path=endpoint)

        # Check status code
        if isinstance(brewery_id, int):
            if 1 <= brewery_id <= 8029:
                assert res.status_code == 200

                res_json = res.json()
                assert isinstance(res_json, dict)

                schema = {
                    "id": {"type": "number", 'required': True},
                    "name": {"type": "string"},
                    "brewery_type": {"type": "string"},
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                    "state": {"type": "string"},
                    "postal_code": {"type": "string"},
                    "country": {"type": "string"},
                    "longitude": {"type": "string", "nullable": True},
                    "latitude": {"type": "string", "nullable": True},
                    "phone": {"type": "string"},
                    "website_url": {"type": "string", "nullable": True},
                    "updated_at": {"type": "string"},
                    "tag_list": {"type": "list"}
                }
                v = cerberus.Validator()
                assert v.validate(res_json, schema), f"Error in brewery:\n {res_json}"

            else:
                assert res.status_code == 404
        elif isinstance(brewery_id, str):
            if brewery_id == "":
                assert res.status_code == 200

                res_json = res.json()
                assert isinstance(res_json, list)

                for brewery in res_json:
                    schema = {
                        "id": {"type": "number", 'required': True},
                        "name": {"type": "string"},
                        "brewery_type": {"type": "string"},
                        "street": {"type": "string"},
                        "city": {"type": "string"},
                        "state": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "country": {"type": "string"},
                        "longitude": {"type": "string", "nullable": True},
                        "latitude": {"type": "string", "nullable": True},
                        "phone": {"type": "string"},
                        "website_url": {"type": "string", "nullable": True},
                        "updated_at": {"type": "string"},
                        "tag_list": {"type": "list"}
                    }
                    v = cerberus.Validator()
                    assert v.validate(brewery, schema), f"Error in brewery:\n {brewery}"

            else:
                assert res.status_code == 404
        else:
            assert False, "Invalid type"
    #

#
