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
        # password is 'password'
        hashed_password='pbkdf2:sha256:150000$7FTGE2c3$1ea0371496f82b298ae582f944120a614cb3e60974c4124bf7ef142fe6a1da90',
        email='theonlyone@stark.com',
        domicile_type='rv',
        phone_number='678-136-7092',
        user_info='I\'m a wealthy American business magnate, playboy, and ingenious scientist. I suffered a severe chest injury during a kidnapping but survived that and kicking @$$ now.',
        createdAt='2021-07-01'
    )

    user2 = User(
        first_name='Bruce',
        last_name='Wayne',
        # password is 'password'
        hashed_password='pbkdf2:sha256:150000$7FTGE2c3$1ea0371496f82b298ae582f944120a614cb3e60974c4124bf7ef142fe6a1da90',
        email='bruce@wayneenterprises.com',
        domicile_type='camper',
        phone_number='221-516-6944',
        user_info='My favorite song goes like: na na na na na na na na na na BATMAN!!!.',
        createdAt='2021-06-21'
    )

    user3 = User(
        first_name='Natasha',
        last_name='Romanoff',
        # password is 'password'
        hashed_password='pbkdf2:sha256:150000$7FTGE2c3$1ea0371496f82b298ae582f944120a614cb3e60974c4124bf7ef142fe6a1da90',
        email='black.widow@avengers.com',
        domicile_type='car',
        phone_number='484-841-6537',
        user_info='I love watching Lost In Translation in the rain.',
        createdAt='2021-05-14'
    )

    user4 = User(
        first_name='Elvis',
        last_name='Presley',
        # password is 'password'
        hashed_password='pbkdf2:sha256:150000$7FTGE2c3$1ea0371496f82b298ae582f944120a614cb3e60974c4124bf7ef142fe6a1da90',
        email='elvis@lives.com',
        domicile_type='car',
        phone_number='373-611-7335',
        user_info='I ain\'t nothin\' but a hound dog.',
        createdAt='2021-02-15'
    )

    demo_user = User(
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
        host_notes='',
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
        host_notes='',
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
        host_notes='',
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
        host_notes='',
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
        host_notes='',
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
        host_notes='',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fpatrick-hendry-euaPfbR6nC0-unsplash.jpg?alt=media&token=dcc8e005-dd14-4e87-a4ca-43ddbdb27d6d", 
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fscott-goodwill-y8Ngwq34_Ak-unsplash.jpg?alt=media&token=48d927cb-6de6-4e4b-b6a5-9f0de7873ea5"],
        title="Nason Creek Campground"
    )

    glacier_campground = Location(
        address='12070 US-2',
        city='West Glacier',
        state='MT',
        gps_coords='48.481785, -113.996492',
        description='Comfy camping area featuring rental cabins, a camp store, laundry facilities & a recreation room.',
        host_notes='Contact this property for rates and availability',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fglacier-1.png?alt=media&token=4f904f8b-1023-4a40-8102-7993a98d7430",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fglacier-2.png?alt=media&token=1c065441-c55c-4fa6-80e8-c5330e15bf51"],
        title="Glacier Campground"
    )

    glacier_campground_nec = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=False,
        max_days=5,
        pad_type='asphalt'
    )

    glacier_campground_amen = Amenity(
        electric_hookup=True,
        water_hookup=True,
        septic_hookup=True,
        assigned_parking=True,
        tow_vehicle_parking=True,
        trash_removal=True,
        water_front=True,
        pets_allowed=True,
        internet_access=True
    )

    glacier_campground.amenity = glacier_campground_amen
    glacier_campground.necessity = glacier_campground_nec
    glacier_campground.user = user1
    db.session.add(glacier_campground)

    stillwater = Location(
        address='8590 US-34',
        city='Granby',
        state='CO',
        gps_coords='40.179674, -105.888878',
        description='Comfy camping area featuring rental cabins, a camp store, laundry facilities & a recreation room.',
        host_notes='Great for kayaking and fishing!',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fstillwater1.png?alt=media&token=22313690-1647-4f6c-8ab2-9ae9e2c372a1",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fstillwater2.png?alt=media&token=bd6fbdc3-fdfe-407f-9c68-453c9f85de70", "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fstillwater3.png?alt=media&token=5c7e8b3b-67ad-4dd2-93c5-ee41b76deab9"],
        title="Stillwater RV and Campground"
    )

    stillwater_nec = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=True,
        max_days=5,
        pad_type='grass & dirt'
    )

    stillwater_amen = Amenity(
        electric_hookup=False,
        water_hookup=True,
        septic_hookup=True,
        assigned_parking=True,
        tow_vehicle_parking=False,
        trash_removal=False,
        water_front=True,
        pets_allowed=True,
        internet_access=False
    )

    stillwater.amenity = stillwater_amen
    stillwater.necessity = stillwater_nec
    stillwater.user = user1
    db.session.add(stillwater)

    west_omaha = Location(
        address='14601 US-6',
        city='Gretna',
        state='NE',
        gps_coords='41.094690, -96.264102',
        description='We are happy to host you through the winter. Our nightly sites will be ELECTRIC ONLY from OCT 28th, 2020 through Apr 1, 2021. We are pleased to announce that as of 1/July/2020 we will be opening our pool and other amenities.',
        host_notes='Contact this property for rates and availability',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fwest_omaha1.png?alt=media&token=6602a9a6-46f1-4ac4-9c78-0e44ec4fe781",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fwest_omaha2.png?alt=media&token=3816ea43-19b3-44dc-a451-ac907dd172c4", "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fwest_omaha3.png?alt=media&token=600656f1-8623-43bf-bcab-a0f34c70cfdf"],
        title="West Omaha"
    )

    west_omaha_nec = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=True,
        max_days=5,
        pad_type='dirt'
    )

    west_omaha_amen = Amenity(
        electric_hookup=False,
        water_hookup=True,
        septic_hookup=True,
        assigned_parking=True,
        tow_vehicle_parking=False,
        trash_removal=False,
        water_front=True,
        pets_allowed=True,
        internet_access=True
    )

    west_omaha.amenity = west_omaha_amen
    west_omaha.necessity = west_omaha_nec
    west_omaha.user = user1
    db.session.add(west_omaha)

    pokegama = Location(
        address='34385 US-2',
        city='Grand Rapids',
        state='MN',
        gps_coords='47.249644, -93.583363',
        description='Mostly RV sites, minimal privacy, lake side with showers and a playground.',
        host_notes='Contact this property for rates and availability',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fpokegama1.png?alt=media&token=b9830c0c-491c-40fe-ba2f-d399b2375126",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Fpokegama2.png?alt=media&token=e529f4ee-5d22-44d7-97e1-cefc31cdeca5"],
        title="Pokegama Dam Campground"
    )

    pokegama_nec = Necessity(
        rv_compatible=True,
        generators_allowed=False,
        fires_allowed=False,
        max_days=2,
        pad_type='grass'
    )

    pokegama_amen = Amenity(
        electric_hookup=False,
        water_hookup=False,
        septic_hookup=False,
        assigned_parking=True,
        tow_vehicle_parking=False,
        trash_removal=False,
        water_front=True,
        pets_allowed=True,
        internet_access=False
    )

    pokegama.amenity = pokegama_amen
    pokegama.necessity = pokegama_nec
    pokegama.user = user1
    db.session.add(pokegama)

    fredericksburg = Location(
        address='5681 East US-290',
        city='Fredericksburg',
        state='TX',
        gps_coords='30.224618, -98.803147',
        description='Located in the heart of the Hill Country, this beautiful KOA is within a few short miles of the area\'s best attractions. Located in the heart of the Hill Country, this beautiful KOA is within a few short miles of the area\'s best attractions. Exclusive shopping, art galleries, elegant dining and the famous National Museum of the Pacific War await you in Fredericksburg. The town has been featured in national magazines for its historic architecture, German culture and heritage, and renowned festivals. Luckenbach, famous for its live country music, is 4 miles away. The Wildseed Farms and Fredericksburg Trade Days, a 350-vendor monthly flea market/collectibles shopping experience, are both within 2 miles.',
        host_notes='We have premium sites with plenty of space for picnics or walking the dogs.',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Ffredericksburg1.png?alt=media&token=ebd20416-880f-434e-83d5-884c4ddeed13",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Ffredericksburg2.png?alt=media&token=7b0546e6-399a-4d8f-8435-03cbb57ed70d"],
        title="Fredericksburg"
    )

    fredericksburg_nec = Necessity(
        rv_compatible=True,
        generators_allowed=False,
        fires_allowed=True,
        max_days=4,
        pad_type='grass & dirt'
    )

    fredericksburg_amen = Amenity(
        electric_hookup=False,
        water_hookup=True,
        septic_hookup=False,
        assigned_parking=True,
        tow_vehicle_parking=False,
        trash_removal=True,
        water_front=True,
        pets_allowed=True,
        internet_access=True
    )

    fredericksburg.amenity = fredericksburg_amen
    fredericksburg.necessity = fredericksburg_nec
    fredericksburg.user = demo_user
    db.session.add(fredericksburg)

    livingston = Location(
        address='15152 US Hwy 190 West',
        city='Onalaska',
        state='TX',
        gps_coords='30.812122, -95.128445',
        description='Welcome to the Lake Livingston/Onalaska KOA! Eddie, the local bald eagle, soars overhead here, and that\'s just one of the many delights at this KOA tucked away in the Piney Woods region of East Texas. The campground wraps along the shore of Lake Livingston, the state\'s second largest lake. It\'s an ideal setting for boating, swimming, fishing for bass and catfish, relaxing and even enjoying a lakefront RV Site. Lakefront amenities include the beautiful beach, a marina(with three ramps, covered slips, transient docks and a fishing pier), a hot tub and a pool. The club-house with a full kitchen is great for reunions, parties and rallies. Enjoy themed weekends(seasonal), planned activities and concessions. Fido will have fun at Kamp K9.',
        host_notes='Contact this property for rates and availability',
        image_urls=[
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Flivingston1.png?alt=media&token=8d869a67-c313-4f63-aae0-a69666c36f83",
            "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Flivingston2.png?alt=media&token=0939dc2b-23b3-4b31-a68a-b8b94951d7a2", "https://firebasestorage.googleapis.com/v0/b/campy-810fc.appspot.com/o/location_images%2Flivingston3.png?alt=media&token=3e5f5b33-1544-4a03-9f80-1165b23682ff"],
        title="Lake Livingston"
    )

    livingston_nec = Necessity(
        rv_compatible=True,
        generators_allowed=True,
        fires_allowed=True,
        max_days=4,
        pad_type='asphalt'
    )

    livingston_amen = Amenity(
        electric_hookup=True,
        water_hookup=True,
        septic_hookup=True,
        assigned_parking=True,
        tow_vehicle_parking=True,
        trash_removal=True,
        water_front=True,
        pets_allowed=True,
        internet_access=True
    )

    livingston.amenity = livingston_amen
    livingston.necessity = livingston_nec
    livingston.user = demo_user
    db.session.add(livingston)

    # asdf = Location(
    #     address='',
    #     city='',
    #     state='',
    #     gps_coords='',
    #     description="",
    #     host_notes='Contact this property for rates and availability',
    #     image_urls=[
    #         "",
    #         ""],
    #     title=""
    # )

    # asdf_nec = Necessity(
    #     rv_compatible=True,
    #     generators_allowed=True,
    #     fires_allowed=True,
    #     max_days=4,
    #     pad_type='asphalt'
    # )

    # asdf_amen = Amenity(
    #     electric_hookup=True,
    #     water_hookup=True,
    #     septic_hookup=True,
    #     assigned_parking=True,
    #     tow_vehicle_parking=True,
    #     trash_removal=True,
    #     water_front=True,
    #     pets_allowed=True,
    #     internet_access=True
    # )

    # asdf.amenity = asdf_amen
    # asdf.necessity = asdf_nec

    # asdf = Location(
    #     address='',
    #     city='',
    #     state='',
    #     gps_coords='',
    #     description="",
    #     host_notes='Contact this property for rates and availability',
    #     image_urls=[
    #         "",
    #         ""],
    #     title=""
    # )

    # asdf_nec = Necessity(
    #     rv_compatible=True,
    #     generators_allowed=True,
    #     fires_allowed=True,
    #     max_days=4,
    #     pad_type='asphalt'
    # )

    # asdf_amen = Amenity(
    #     electric_hookup=True,
    #     water_hookup=True,
    #     septic_hookup=True,
    #     assigned_parking=True,
    #     tow_vehicle_parking=True,
    #     trash_removal=True,
    #     water_front=True,
    #     pets_allowed=True,
    #     internet_access=True
    # )

    # asdf.amenity = asdf_amen
    # asdf.necessity = asdf_nec

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

    db.session.add(demo_user)
    db.session.add(location1)
    db.session.add(location2)
    db.session.commit()
