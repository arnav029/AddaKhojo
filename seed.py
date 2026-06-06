import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aawaaragardi.settings')
django.setup()

from places.models import Place

places_data = [
    {
        'name': 'Egg Roll Uncle',
        'type': 'thela',
        'is_on_google': False,
        'sector': 'Sector 3',
        'location_text': 'footpath near 27th Main, right side',
        'timings_text': 'evenings only, ~6pm to 9pm',
        'price_text': 'Rs 30',
        'vibe_tag': 'worth_the_detour',
        'caption': 'Rs 30 of pure joy. Uncle calls everyone boss and adds extra chilli if you smile. Sells out by 9 — do not be a hero. Stand, eat, get messy, leave happy.',
        'practical_notes': 'cash only · sells out by 9pm · no seating',
        'status': 'published',
    },
    {
        'name': 'The Quiet Garden',
        'type': 'garden',
        'is_on_google': False,
        'sector': 'Sector 3',
        'location_text': 'behind the white temple, unnamed gate',
        'timings_text': 'dawn to dusk',
        'price_text': 'free',
        'vibe_tag': 'calm_o_meter_max',
        'caption': 'No name, no gate-board, no crowd. One bench under a gulmohar tree. Perfect for a 7am chai, a phone call you are avoiding, or a small existential crisis.',
        'practical_notes': 'no lights after dark · best at sunrise',
        'status': 'published',
    },
    {
        'name': 'Mixnotion Cafe',
        'type': 'cafe',
        'is_on_google': True,
        'sector': 'HSR Layout',
        'location_text': '18th Cross, near BDA Complex',
        'timings_text': '9am-11pm',
        'price_text': 'Rs 500 for two',
        'vibe_tag': 'local_favourite',
        'caption': 'Yes it is on Google — but nobody told you the corner table has the best light at 4pm, or that the off-menu filter coffee is the real move. We are telling you. Go.',
        'practical_notes': 'plugs available · gets crowded on weekends',
        'status': 'published',
    },
]

for data in places_data:
    if not Place.objects.filter(name=data['name']).exists():
        Place.objects.create(**data)
        print(f"Created: {data['name']}")
    else:
        print(f"Already exists: {data['name']}")

print('Seeding done.')
