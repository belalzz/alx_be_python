weather_status = input("What's the weather like today? (sunny/rainy/cold): ")
responses = {'sunny':'Wear a t-shirt and sunglasses.',
             'rainy': 'Don\'t forget your umbrella and a raincoat.',
             'cold' :'Make sure to wear a warm coat and a scarf.'}
if (weather_status in responses):
    print(responses[weather_status])
else:
    print("Sorry, I don't have recommendations for this weather.")