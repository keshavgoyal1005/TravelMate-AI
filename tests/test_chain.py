from app.llm.chains import travel_chain


def test_travel_chain():
    response = travel_chain.invoke(
        {
            "user_request": "Plan a 5-day trip to Goa"
        }
    )

    print(response.content)

    assert response.content
    