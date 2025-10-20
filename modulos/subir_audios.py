import aiohttp
import os

async def subirAudio(mensaje,archivo):
    async with aiohttp.ClientSession() as session:
        async with session.get(mensaje) as response:
            if response.status == 200: # codigo de estado http = "ok"
                print("Estatus: ", response.status)
                with open(archivo, 'wb') as f:
                    f.write(await response.read())
                print("Se descargo correctamente")
                return archivo
            else:
                print("Error, status: ", response.status)
                return None


"""
        <h1> testestes</h1>
        <p2> Lorem ipsum dolor, sit amet consectetur adipisicing elit. Possimus adipisci accusamus doloremque neque, fugit a reiciendis. Placeat dolorum rem maxime. Porro provident quam atque commodi cum molestiae minima quaerat quod?</p2>"""
"""

h1{

    background-color: #7289da;
    text-align: center;
    margin: auto;
    width: 50%;
    height: 50%;
}"""