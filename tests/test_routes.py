def test_get_all_returns_200_and_empty_array(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, sample_data_with_two_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"id":1,
                            "name":"Ocean Planet",
                            "description":"It's wet!",
                            "has_moons":True}

def test_get_one_planet_without_data_returns_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"details":"Planet id: 1 not found"}

def test_get_all_planets(client, sample_data_with_two_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id":1,
                            "name":"Ocean Planet",
                            "description":"It's wet!",
                            "has_moons":True},
                            {"id":2,
                            "name":"Jungle Planet",
                            "description":"Full of big cats. And trees!",
                            "has_moons":False}] 

def test_create_a_planet(client):
    # Act
    response = client.post("/planets", json={
        "name":"Ice Planet",
        "description":"Right next to Canada",
        "has_moons":True
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {"details":"Planet Ice Planet successfully added to the Planets Database."}

def test_update_planet_patches_properly(client, sample_data_with_two_planets):
    pre_patch_response = {
                "name":"Ocean Planet",
                "id":1,        
                "description":"It's wet!",
                "has_moons":True}
    pre_patch_response_body = pre_patch_response.get_json()
    
    response = client.patch("/planets/1", json={"description":"It's wet and full of fish."})
    response_body= response.get_json()

    assert response.status_code == 200
    assert response_body["description"] == "It's wet and full of fish."
    assert response_body["name"] == pre_patch_response_body["name"]
    assert response_body["has_moons"] == pre_patch_response_body["has_moons"]
    assert response_body["id"] == pre_patch_response_body["id"]
    assert response_body["description"] != pre_patch_response_body["description"]


