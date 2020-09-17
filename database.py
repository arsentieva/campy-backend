from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models.models import (
    User, Calendar, Trip,
    Amenity, Necessity, Location, Review)

with app.app_context():
    db.drop_all()
    db.create_all()

    # 4 users
    # 6 locations
    # 3 reviews

    user1 = User(
        first_name='Tony',
        last_name='Stark',
        hashed_password='asdfasdf',
        email='theonlyone@stark.com',
        domicile_type='rv',
        phone_number='678-136-7092',
        user_info='I\'m a wealthy American business magnate, playboy, and ingenious scientist. I suffered a severe chest injury during a kidnapping but survived that and kicking @$$ now.',
        createdAt='2021-07-01'
    )

    user2 = User(
        first_name='Bruce',
        last_name='Wayne',
        hashed_password='asdfasdf',
        email='bruce@wayneenterprises.com',
        domicile_type='camper',
        phone_number='221-516-6944',
        user_info='My favorite song goes like: na na na na na na na na na na BATMAN!!!.',
        createdAt='2021-06-21'
    )

    user3 = User(
        first_name='Natasha',
        last_name='Romanoff',
        hashed_password='asdfasdf',
        email='black.widow@avengers.com',
        domicile_type='car',
        phone_number='484-841-6537',
        user_info='I love watching Lost In Translation in the rain.',
        createdAt='2021-05-14'
    )

    user4 = User(
        first_name='Elvis',
        last_name='Presley',
        hashed_password='asdfasdf',
        email='elvis@lives.com',
        domicile_type='car',
        phone_number='373-611-7335',
        user_info='I ain\'t nothin\' but a hound dog.',
        createdAt='2021-02-15'
    )

    user5 = User(
        first_name='Demo',
        last_name='User',
        hashed_password='pbkdf2:sha256:150000$7FTGE2c3$1ea0371496f82b298ae582f944120a614cb3e60974c4124bf7ef142fe6a1da90',
        email="demo@email.com",
        domicile_type='car',
        phone_number='555-555-5555',
        user_info='I\'m a demo user...take a look around.',
        createdAt='2021-02-15'
    )

    location1_amenity = Amenity(
        electric_hookup=True,
        water_hookup=True,
        septic_hookup=False,
        assigned_parking=False,
        tow_vehicle_parking=True,
        trash_removal=False,
        water_front=True,
        pets_allowed=True,
        internet_access=False
    )

    location2_amenity = Amenity(
        electric_hookup=True,
        water_hookup=True,
        septic_hookup=False,
        assigned_parking=False,
        tow_vehicle_parking=False,
        trash_removal=True,
        water_front=False,
        pets_allowed=True,
        internet_access=True
    )

    location1_neces = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=True,
        max_days=2,
        pad_type='grass'
    )

    location2_neces = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=True,
        max_days=5,
        pad_type='dirt'
    )

    location1 = Location(
        address='10880 Malibu Point',
        city='Malibu',
        state='CA',
        gps_coords='34.000872,-118.806839',
        description='It overlooks the Pacific Ocean with an amazing view. It was once destroyed from a very unfortunate happening, but now rebuilt like it never happened. Might find some interesting things down the basement.',
        host_notes='Have fun and then get out. Also, don\'t touch things without permission.',
        image_urls=[
         "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fzibik-A6OHsnGYd18-unsplash.jpg?alt=media&token=664286fb-0285-41b0-8c8c-2ab511f17d09",
         "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fblake-wisz-TcgASSD5G04-unsplash.jpg?alt=media&token=3edb60be-b096-4c2f-87e9-68df6eec20a5"],
        title="Home away from home."
    )

    location2 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='ZE',
        gps_coords='-3.66105, 144.52694',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
          "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fbrooks-rice-8-jqqr-rpo0-unsplash.jpg?alt=media&token=4ffe2679-eaff-41ac-b890-bd585bb8573d",
          "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fcameron-vaughan-0AV7XLABuZk-unsplash.jpg?alt=media&token=a181c0d6-2426-4e31-8843-2c54473b8461"],
        title="Stay Happy Place"
    )

    location3 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='47.959, -120.539',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
         "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fcameron-vaughan-0AV7XLABuZk-unsplash.jpg?alt=media&token=a181c0d6-2426-4e31-8843-2c54473b8461blake-wisz-TcgASSD5G04-unsplash.jpg",
         "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fdino-reichmuth-5Rhl-kSRydQ-unsplash.jpg?alt=media&token=907439e7-055f-46e4-9124-aa99d6b950f4"],
        title="Silver Falls Group Site"
    )

    location3 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='48.0937, -120.313',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fdino-reichmuth-pl1mhwMctJc-unsplash.jpg?alt=media&token=0a5b0aa0-1c89-4372-9731-cb1f765b3433",
             "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fdominik-jirovsky-re2LZOB2XvY-unsplash.jpg?alt=media&token=b456d772-c4cf-4f5b-b8eb-4a903e4928ba"],
        title="Okanogan-Wenatchee Forest"
    )

    location4 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='47.7586, -120.425',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fedho-fitrah-ELevCx8PX4o-unsplash.jpg?alt=media&token=34726190-865e-48c0-b5a6-2db7eb8b756c", 
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Feric-muhr-ZPsJW-OLZQM-unsplash.jpg?alt=media&token=b808f44d-1b63-4bf3-aa0b-43fc7d975d63"],
        title="Pine Flats Group Campground"
    )

    location5 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='48.02095, -120.641',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fjonathan-forage-1azAjl8FTnU-unsplash.jpg?alt=media&token=c91ee4c3-b653-4ece-9009-1c8433af9232",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fjosh-hild-8f_VQ3EFbTg-unsplash.jpg?alt=media&token=4910bf97-62c2-45cc-80aa-bf3e58049e93"],
        title="Cottonwood Cabin"
    )

    location6 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='47.896667, -120.698',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Flaura-pluth-RMicIhNOOIg-unsplash.jpg?alt=media&token=d81563cc-d6f3-44c5-9883-b350cc6ccbf9", 
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fmike-erskine-S_VbdMTsdiA-unsplash.jpg?alt=media&token=f9fc0db1-6ac8-4f18-acfc-130ec8ba4f4d"],
        title="Grouse Creek Group Site"
    )

    location7 = Location(
        address='25218 Eu St.',
        city='Banjarmasin',
        state='WA',
        gps_coords='47.799, -120.716',
        description='Has world class museums, and gardens. It has an well developed walkable river front on the edge of downtown where various events are held.',
        host_notes='I\'m sad, so sad',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fpatrick-hendry-euaPfbR6nC0-unsplash.jpg?alt=media&token=dcc8e005-dd14-4e87-a4ca-43ddbdb27d6d", 
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fscott-goodwill-y8Ngwq34_Ak-unsplash.jpg?alt=media&token=48d927cb-6de6-4e4b-b6a5-9f0de7873ea5"],
        title="Nason Creek Campground"
    )

    review1 = Review(
        overall_rating=4,
        noise=5,
        safety=4,
        cleanliness=5,
        access=1,
        site_quality=5,
        comments='Host is very lovely, the location was perfect and the parking easy.'
    )

    review2 = Review(
        overall_rating=3,
        noise=1,
        safety=4,
        cleanliness=3,
        access=4,
        site_quality=5,
        comments='This is a lovely spot, and a kind and generous host. The neighborhood is peaceful and beautiful, as well as easily walkable to shops and restaurants. A really terrific place to stay.'
    )

    review3 = Review(
        overall_rating=3,
        noise=3,
        safety=3,
        cleanliness=3,
        access=3,
        site_quality=3,
        comments='Hosts were welcoming and generous. Their little spot in the heart of this upscale area of Portland gave me and Journey (my dog) a walkable neighborhood to enjoy. I also relished the porch chats with our hosts, which were full of local history and politics, and a long walking tour of the neighborhood.'
    )

    location1.amenity = location1_amenity
    location1.necessity = location1_neces
    location1.user = user1

    location2.amenity = location2_amenity
    location2.necessity = location2_neces
    location2.user = user2

    location3.amenity = location2_amenity
    location3.necessity = location2_neces
    location3.user = user2

    location4.amenity = location2_amenity
    location4.necessity = location2_neces
    location4.user = user2

    location5.amenity = location2_amenity
    location5.necessity = location2_neces
    location5.user = user2

    location6.amenity = location2_amenity
    location6.necessity = location2_neces
    location6.user = user2

    location7.amenity = location2_amenity
    location7.necessity = location2_neces
    location7.user = user2

    review1.location = location1
    review1.user = user3
    review2.location = location1
    review2.user = user4
    review3.location = location2
    review3.user = user4

    db.session.add(user5)
    db.session.add(location1)
    db.session.add(location2)
    db.session.commit()
