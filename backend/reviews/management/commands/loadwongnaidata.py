import csv
import os
from django.core.management.base import BaseCommand

from ...models import Review, Tag


class Command(BaseCommand):
    help = "Load wongnai corpus to database"

    def add_arguments(self, parser):
        parser.add_argument("dir", type=str)

    def handle(self, *args, **kwargs):
        base_dir = kwargs["dir"]
        food_txt = os.path.join(base_dir, "food_dictionary.txt")
        review_csv = os.path.join(base_dir, "test_file.csv")

        with open(food_txt) as f:
            print("Loading foods...")
            for idx, line in enumerate(f):
                if idx == 20000:
                    break
                Tag.objects.get_or_create(name=line.strip())
            print("Finish!")

        with open(review_csv) as f:
            print("Loading reviews...")
            reader = csv.reader(f, delimiter=";")
            next(reader)
            lines = [line for line in reader]
            for line in lines:
                Review.objects.create(content=line[1])
            print("Finish!")

