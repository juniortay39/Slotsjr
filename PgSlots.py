import random
import time
import asyncio
from telethon import TelegramClient, events

# Dados do bot
api_id = '29636471'
api_hash = 'd9029baff362d945efbdb6b96b83802b'
bot_token = '7330620127:AAFN8wD4GPHNXR_-m8Rj06btAkdskTpszWg'
chat_id = -4578137928  # Note the negative ID

# URLs das imagens no Imgur associadas a cada jogo
game_images = {
    "Fortune Tiger": "https://i.imgur.com/QPdyYdX.jpeg",
    "Fortune Ox": "https://i.imgur.com/aFYCcw5.jpeg",
    "Fortune Mouse": "https://i.imgur.com/ZJAQJKh.jpeg",
    "Fortune Dragon": "https://i.imgur.com/YCJmmsW.jpeg",
    "Fortune Rabbit": "https://i.imgur.com/xDlRQSk.jpeg"
}

# Lista de nomes de jogos
games = list(game_images.keys())

# Função para gerar um sinal aleatório
def generate_signal():
    game = random.choice(games)
    normal_spins = random.randint(4, 12)
    turbo_spins = random.randint(4, 10)
    bet_level = random.randint(4, 7)
    return {
        "game": game,
        "normal_spins": normal_spins,
        "turbo_spins": turbo_spins,
        "bet_level": bet_level
    }

# Função para enviar um sinal no Telegram com a imagem correspondente ao jogo
async def send_signal_with_image(signal):
    game_icon = {
        "Fortune Tiger": "🐯",
        "Fortune Mouse": "🐭",
        "Fortune Rabbit": "🐰",
        "Fortune Ox": "🐮",
        "Fortune Dragon": "🐲"
    }

    # Construir e enviar a mensagem de sinal com a imagem correspondente ao jogo
    message = f"🚨⚔️ **ENTRADA CONFIRMADA** ⚔️🚨\n{game_icon[signal['game']]} {signal['game']}\n⚔️ ATAQUE EM MASSA\n🌎 Horário De Brasília\n\n⏰ **Estratégia**: intercalando\n\n💰 {signal['normal_spins']}x **Normal**\n💰 {signal['turbo_spins']}x **Turbo**\n🆙 Nível de aposta: {signal['bet_level']}\n⚡️ **Intercalando**\n⚠ **Validade**: dois minutos\n\n📌 **Dica**: Alterne os giros entre normal e turbo, e se vier um Grande Ganho, PARE, e espere o próximo ATAQUE EM MASSA ⚔\n\n💲 **Banca Recomendada**: R$20,00\n🚨 **Atenção**: bote no mínimo o valor recomendado para sua banca subir rápido e você obter maiores lucros.\n\n💸[Cadastre-se](https://cl1ca.com/GanharAgora) e Deposite na Plataforma com a Falha do momento!💸\n💸Depósito Mínimo R$1,00 - Pegue Este Sinal e Lucre Agora💸"
    
    # Enviar a imagem e a mensagem no Telegram
    await client.send_file(chat_id, game_images[signal['game']], caption=message)

    # Aguardar 2 minutos
    await asyncio.sleep(120)

    # Enviar mensagem de fim de validade
    final_message = f"✅⚔️ **ENTRADA FINALIZADA** ⚔️✅\n{game_icon[signal['game']]} {signal['game']}\n\n💲 **Banca Recomendada**: R$20,00\n🚨 **Atenção**: bote no mínimo o valor recomendado para sua banca subir rápido e você obter maiores lucros.\n\n💸[Cadastre-se](https://cl1ca.com/GanharAgora) e Deposite na Plataforma com a Falha do momento!💸\n💸Depósito Mínimo R$1,00 - Espere o Próximo Sinal para Lucrar!💸"
    
    await client.send_message(chat_id, final_message)

    # Aguardar 1 minuto após a mensagem de finalização
    await asyncio.sleep(60)

    # Enviar a mensagem "FUNCIONA APENAS NESTA PLATAFORMA"
    platform_message = ("🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️\n"
                        "🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: [Clique Aqui & Cadastre-se](https://cl1ca.com/GanharAgora)\n\n"
                        "⚠️ NÃO TENTE EM OUTRO SITE! ⬆️\n"
                        "✅ *ATENÇÃO PLATAFORMA NOVA!*\n"
                        "⭐️ ANALISAMOS TODOS OS JOGOS DA PG SOFT!\n"
                        "⭐️ ENVIAMOS APENAS OS QUE TEM CHANCE DE PAGAR!\n"
                        "💻 PLATAFORMA NOVA PAGA MUITOOOO!")

    platform_message_id = await client.send_message(chat_id, platform_message)

    return platform_message_id

# Função para deletar a mensagem "FUNCIONA APENAS NESTA PLATAFORMA"
async def delete_platform_message(message_id):
    await client.delete_messages(chat_id, message_id)

# Criação do cliente Telegram com bot token
client = TelegramClient('bot_session', api_id, api_hash)

# Autenticação do bot
async def main():
    await client.start(bot_token=bot_token)

    # Loop infinito para enviar sinais a cada 2, 3, 4 ou 5 minutos
    while True:
        signal = generate_signal()
        platform_message_id = await send_signal_with_image(signal)
        
        # Esperar entre 1 e 4 minutos (tempo aleatório)
        wait_time = random.randint(2, 5) * 60

        # Deletar a mensagem 10 segundos antes de enviar o novo sinal
        await asyncio.sleep(wait_time - 10)
        await delete_platform_message(platform_message_id)

        # Aguardar os 10 segundos restantes antes de enviar o próximo sinal
        await asyncio.sleep(10)

# Execução do código
asyncio.run(main())
