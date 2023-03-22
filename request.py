import asyncio

import httpx


async def print_repos():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            'https://api.github.com/users/davilos/repos'
        )
        data = response.json()

        print('Meus repositórios:')
        for repo in data:
            try:
                print(
                    f"Nome: {repo['name']}\nPrivado: {repo['private']}\nURL: {repo['html_url']}\nLicense: {repo['license']['name']}"
                )
                print('-=' * 50)
            except TypeError:
                print(
                    f"Nome: {repo['name']}\nPrivado: {repo['private']}\nURL: {repo['html_url']}\nLicense: None"
                )
                print('-=' * 50)


def main():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(print_repos())
    loop.close()


main()
