"""Module to generate random users"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

fake = faker.Faker()
logging.basicConfig(
    level=logging.INFO,
    filename=BASE_DIR / 'user.log',
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_user():
    """Generate a single user.

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
    """Generate a list of users

    Args:
        n (int): Nomber of user to generate

    Returns:
        list[str]: users
    """
    logging.info(f"Generate a list of {n} users.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(n=5)
    print(user)
