from sys import path_importer_cache
import tracemalloc
from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.tl.functions.help import GetUserInfoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import EditMessageRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import errors
import google_trans_new as gtn
import speech_recognition as sr
from pydub import AudioSegment
import requests
from gtts import gTTS
import moviepy.editor as mp
from pathlib import Path
from os.path import exists
import os
import random
import time

#my_secret = os.environ['API_ID_SECRET']
#api_id = my_secret
#my_secret = os.environ['API_HASH_SECRET']
#api_hash = my_secret

api_id = input("inserire API ID: ")
api_hash = input("inserire Hash ID: ")
cm = input(
  "Digita il simbolo identificativo per i comandi ('!', '.' , '-' ecc...\nEs: !comandi .comandi\nAttenzione: il simbolo '?' non può essere utilizzato.\nDigita la tua scelta: "
)

client = TelegramClient('session_name', api_id, api_hash)
client.start()

alf = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
  '3', '4', '5', '6', '7', '8', '9'
]

language = 'it'
casca = ''
spazio = ' '
punto = '.'
otto = '8'
duepunti = ':'
d = 'D'

prec = None
response = None
info = []
conteggio = False
bloccato = False
multisticker = False
chat = 0
numero_stick = 0
numeri_lista = []
for i in range(25):
  numeri_lista.append(str(i))

me = client.get_me()
user_uname = me.username
user_full = client(GetFullUserRequest(me.username))
#print(user_full)
user_about = user_full.full_user.about
user_name = me.first_name
user_path = str(Path().absolute())
file_exists = exists(user_uname + '.jpg')
if (file_exists):
  os.remove(user_uname + '.jpg')
client.download_profile_photo(user_uname)

#FILE PARZIALE
f = open("info.txt", "w", encoding="utf-8")
f.write(user_name + "\r\n")
f.write(str(user_about))
f.close()
#FILE TOTALE
f = open("info_tot.txt", "w", encoding="utf-8")
f.write(user_name + "\r\n")
f.write(str(user_about))
f.close()

print(user_path)

print(client.get_me().stringify())
print("\n\n\nPollPolac È IN FUNZIONE\n")
salva_file = True

messages = client.get_messages(user_uname)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'comandi'))
async def handler(event):
  await event.edit("""LISTA COMANDI:
    
(WARNING --> Prima di ogni comando digitare il simbolo identificativo scelto in fase di avvio.
Esempio: !comandi, -comandi, .comandi ecc...)

- copia: copia il profilo di un utente e aggiunge i dati al tuo account (nome, bio, pic)
- reset parziale: rimette i dati precedenti alla copiatura di un profilo (se non si ha copiato vengono reimpostati i dati originali)
- reset totale: rimette i dati iniziali
- aggiorna: aggiorna i dati salvati (utile per quando si utilizza il comando !reset parziale o !reset totale)
- stalker: invia informazioni di un profilo (il comando dev'essere usato in risposta a un messaggio)
- stick: usa il comando in risposta a un messaggio per trasformare questo in uno sticker statico
- mstick: usa il comando in risposta a un messaggio per trasformare questo in uno sticker animato
- blocca: rispondi al messaggio di un utente per bloccarlo
- sblocca: rispondi al messaggio di un utente per sbloccarlo
- ghostmode: il tuo profilo diventa uguale a un account eliminato (nome e pic)
- ghostreset: analogo a !reset totale, reimposta il profilo coi dati iniziali
- pic: rispondi al messaggio di un utente per copiargli la pic e impostarla sul tuo profilo
- tras: trascrive il messaggio audio di un utente (comando da utilizzare in risposta al messaggio desiderato)
- speak: converte un messaggio da testo ad audio (comando da utilizzare in risposta al messaggio desiderato)
- trit: traduzione di un messaggio in italiano (comando da utilizzare in risposta al messaggio desiderato)
- tren: traduzione di un messaggio in inglese (comando da utilizzare in risposta al messaggio desiderato)
- foto persona: invia la foto di una persona inesistente
- foto anime: invia la foto di un anime inesistente
- foto gatto: invia la foto di un gatto inesistente
- dona/!donazione: supporta il creatore 😊
    
""")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'stalker'))
async def handler(event):
  global prec, response
  message = await event.get_reply_message()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    chat = message.chat_id
    if (message.from_id == None):
      sender = await client.get_entity(message.peer_id)
    else:
      sender = await client.get_entity(message.from_id)
    print(sender)

    async with client.conversation(chat) as conv:

      try:
        await client.forward_messages(461843263, message)
        for i in range(3):
          response = conv.wait_event(
            events.NewMessage(incoming=True, from_users=461843263))

          response = await response

          if response.text.startswith("send"):
            await event.edit(
              "```can you kindly disable your forward privacy settings for good?```"
            )
          else:
            await event.respond(response.message.message)
      except YouBlockedUserError:
        print(YouBlockedUserError)
        await event.reply(
          "```Please unblock @sangmatainfo_bot and try again```")
        return


@client.on(events.NewMessage(pattern='(?i)' + cm + 'stick'))
async def handler(event):
  global chat
  message = await event.get_reply_message()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    chat = message.chat_id

    await client.forward_messages("@QuotLyBot", message)

    await event.edit("sticker creato con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'mstick'))
async def handler(event):
  global chat
  message = await event.get_reply_message()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    chat = message.chat_id

    if (message.media):
      if (message.video):
        await client.send_file("@toWebmBot", message)
      else:
        await client.send_file("@Stickerdownloadbot", message)

      await event.edit("sticker creato con successo!")
    else:
      await event.edit("il messaggio selezionato non è un video/gif!")


@client.on(events.NewMessage(chats="@QuotLyBot"))
async def handler(event):
  await client.send_file(chat, event.message)


@client.on(events.NewMessage(chats="@toWebmBot"))
async def handler(event):
  global chat
  if (event.message.media):
    await client.forward_messages(chat, event.message)


@client.on(events.NewMessage(chats="@Stickerdownloadbot"))
async def handler(event):
  global chat, conteggio

  if (event.message.media and conteggio):
    await client.send_file(chat, event.message)
  else:
    conteggio = True


@client.on(events.NewMessage(pattern='(?i)' + cm + 'blocca'))
async def handler(event):
  k = event.message.text.strip().split(" ")
  lunghezza = len(k)
  verr = True
  print(k)
  print(lunghezza)
  try:
    message = await event.get_reply_message()
    print(message)
  except Exception as e:
    print("1")
    print(e)
  if (lunghezza >= 2):
    verr = False
  try:
    if (verr):
      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):
        if (message.from_id == None):
          sender = await client.get_entity(message.peer_id)
        else:
          sender = await client.get_entity(message.from_id)

        await client(functions.contacts.BlockRequest(id=sender.id))
        await event.edit('utente bloccato!')
    else:
      cont = 0
      for c in k:
        cont = cont + 1
        print(c)
        if (cont == 2):
          t = c
      todo = await client(GetFullUserRequest(t))
      print(t)

      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):

        await client(functions.contacts.BlockRequest(id=todo.user.id))
        await event.edit('utente bloccato!')
  except Exception as e:
    print("2")
    print(e)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'sblocca'))
async def handler(event):
  k = event.message.text.strip().split(" ")
  lunghezza = len(k)
  verr = True
  print(k)
  print(lunghezza)
  try:
    message = await event.get_reply_message()
    print(message)
  except Exception as e:
    print("1")
    print(e)
  if (lunghezza >= 2):
    verr = False
  try:
    if (verr):
      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):
        if (message.from_id == None):
          sender = await client.get_entity(message.peer_id)
        else:
          sender = await client.get_entity(message.from_id)

        await client(functions.contacts.UnblockRequest(id=sender.id))
        await event.edit('utente sbloccato!')
    else:
      cont = 0
      for c in k:
        cont = cont + 1
        print(c)
        if (cont == 2):
          t = c
      todo = await client(GetFullUserRequest(t))
      print(t)

      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):

        await client(functions.contacts.UnblockRequest(id=todo.full_user.id))
        await event.edit('utente sbloccato!')
  except Exception as e:
    print("2")
    print(e)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'spam'))
async def handler(event):
  k = event.message.text.strip().split(" ")
  lunghezza = len(k)
  verr = False
  testo = ""
  print(k)
  print(lunghezza)
  if (lunghezza >= 3):
    verr = True
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    if (verr):
      cont = 0
      for c in k:
        cont = cont + 1
        print(c)
        if (cont == 2):
          n = c
        if (cont >= 3):
          testo = testo + c + " "
          #testo.append(" ")
      for i in range(int(n)):
        await event.respond(testo)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'ghostmode'))
async def handler(event):
  if (event.message.from_id == None):
    sender_main = await client.get_entity(event.message.peer_id)
  else:
    sender_main = await client.get_entity(event.message.from_id)
  me = await client.get_me()
  user_uname = me.username
  user_full = await client(GetFullUserRequest(me.username))
  user_about = user_full.full_user.about
  user_name = me.first_name
  if (sender_main.username == me.username):
    #FILE TOTALE
    f = open("info.txt", "w", encoding="utf-8")
    f.write(user_name + "\r\n")
    f.write(str(user_about))
    f.close()
    file_exists = exists('gost.jpg')
    if (file_exists):
      await client(
        UpdateProfileRequest(first_name='Account eliminato', about=' '))
      await client(
        UploadProfilePhotoRequest(await client.upload_file('gost.jpg')))
      await event.edit("ghostmode attivata con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'pic'))
async def handler(event):
  message = await event.get_reply_message()

  if (event.message.from_id == None):
    sender_main = await client.get_entity(event.message.peer_id)
  else:
    sender_main = await client.get_entity(event.message.from_id)
  me = await client.get_me()
  user_uname = me.username
  user_full = await client(GetFullUserRequest(me.username))
  user_about = user_full.full_user.about
  user_name = me.first_name
  if (sender_main.username == me.username):
    file_exists = exists('copia.jpg')
    if (file_exists):
      os.remove('copia.jpg')
    if (message.media):
      path = await message.download_media()
      if (message.video):
        file_exists = exists('copia.mp4')
        if (file_exists):
          os.remove('copia.mp4')
        print(path)
        os.rename(path, "copia.mp4")
        clip = mp.VideoFileClip("copia.mp4")
        clip_resized = clip.resize(width=800, height=800)
        clip_resized.write_videofile("copia.mp4")
        await client(
          UploadProfilePhotoRequest(await client.upload_file('copia.mp4')))
      if (message.photo):
        file_exists = exists('copia.jpg')
        if (file_exists):
          os.remove('copia.jpg')
        print(path)
        os.rename(path, "copia.jpg")
        await client(
          UploadProfilePhotoRequest(await client.upload_file('copia.jpg')))

    await event.edit("pic aggiornata con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'aggiorna'))
async def handler(event):
  me = await client.get_me()
  user_uname = me.username
  user_full = await client(GetFullUserRequest(me.username))
  user_about = user_full.full_user.about
  user_name = me.first_name
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    file_exists = exists(user_uname + '.jpg')
    if (file_exists):
      os.remove(user_uname + '.jpg')
    await client.download_profile_photo(user_uname)
    #FILE TOTALE
    f = open("info_tot.txt", "w", encoding="utf-8")
    f.write(user_name + "\r\n")
    f.write(str(user_about))
    f.close()
    await event.edit("aggiornamento dati eseguito con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'copia'))
async def handler(event):
  global salva_file
  global user_name
  global user_about
  global user_uname
  k = event.message.text.strip().split(" ")
  lunghezza = len(k)
  verr = True
  print(k)
  print(lunghezza)
  try:
    message = await event.get_reply_message()
    print(message)
  except Exception as e:
    print("1")
    print(e)
  if (lunghezza >= 2):
    verr = False
  try:
    if (verr):
      #COPIATURA
      #Verifica utente (main)
      me = await client.get_me()
      id_main = event.id
      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):
        #Analisi messaggio inviato
        id = event.reply_to_msg_id
        message = await event.get_reply_message()
        print(message)
        if (message.from_id == None):
          sender = await client.get_entity(message.peer_id)
        else:
          sender = await client.get_entity(message.from_id)
        print(sender)
        ##SALVATAGGIO INFO USER ATTUALI##
        if (salva_file):
          user_uname = me.username
          user_full = await client(GetFullUserRequest(me.username))
          user_about = user_full.full_user.about
          user_name = me.first_name
          salva_file = False
        #else:

        #################################
        #SALVATAGGIO NEL PROFILO
        f = open("info.txt", "w", encoding="utf-8")
        f.write(user_name + "\r\n")
        f.write(str(user_about) + "\r\n")
        f.write(user_uname)
        f.close()

        todo = await client(GetFullUserRequest(sender.username))
        print(todo.full_user.id)
        user_uname = sender.username
        user_about = todo.full_user.about
        user_name = sender.first_name

        file_exists = exists(sender.username + '.jpg')
        if (file_exists):
          os.remove(sender.username + '.jpg')
        await client.download_profile_photo(sender.username)
        full = await client(GetFullUserRequest(sender.username))
        await client(
          UpdateProfileRequest(first_name=sender.first_name,
                               about=full.full_user.about))
        await client(
          UploadProfilePhotoRequest(await client.upload_file(sender.username +
                                                             '.jpg')))
      await event.edit("copia dati eseguita con successo!")
    else:
      cont = 0
      for c in k:
        cont = cont + 1
        print(c)
        if (cont == 2):
          t = c
      todo = await client(GetFullUserRequest(t))
      print(t)
      #COPIATURA
      #Verifica utente (main)
      me = await client.get_me()
      id_main = event.id
      message_main = event.message
      if (message_main.from_id == None):
        sender_main = await client.get_entity(message_main.peer_id)
      else:
        sender_main = await client.get_entity(message_main.from_id)

      if (sender_main.username == me.username):
        #Analisi messaggio inviato
        ##SALVATAGGIO INFO USER ATTUALI##
        if (salva_file):
          user_uname = me.username
          user_full = await client(GetFullUserRequest(me.username))
          user_about = user_full.full_user.about
          user_name = me.first_name
          salva_file = False

        #################################
        #SALVATAGGIO NEL PROFILO
        f = open("info.txt", "w", encoding="utf-8")
        f.write(user_name + "\r\n")
        f.write(str(user_about) + "\r\n")
        f.write(user_uname)
        f.close()

        print(todo.full_user.id)
        user_uname = t
        user_about = todo.full_user.about
        print("131903103910\n\n\n")
        print(todo.users[0].first_name)
        user_name = todo.users[0].first_name

        p = t.replace("@", "")
        print(p)
        file_exists = exists(p + '.jpg')
        if (file_exists):
          os.remove(p + '.jpg')
        p = await client.download_profile_photo(t)
        print(p)
        full = await client(GetFullUserRequest(t))
        await client(
          UpdateProfileRequest(first_name=full.users[0].first_name,
                               about=full.full_user.about))
        await client(UploadProfilePhotoRequest(await client.upload_file(p)))
      await event.edit("copia dati eseguita con successo!")
  except Exception as e:
    print("2")
    print(e)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'reset parziale'))
async def handler(event):
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    f = open("info.txt", "r", encoding="utf-8")
    contents = f.readlines()
    i = 0
    for content in contents:
      if (i == 0):
        user_name = content
      elif (i == 1):
        user_about = content
      else:
        user_uname = content
      i = i + 1
    await client(UpdateProfileRequest(first_name=user_name, about=user_about))
    await client(
      UploadProfilePhotoRequest(await client.upload_file(user_uname + '.jpg')))
    f.close()
    await event.edit("i dati precedenti sono stati copiati con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'reset totale'))
async def handler(event):
  global me
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    f = open("info_tot.txt", "r", encoding="utf-8")
    contents = f.readlines()
    i = 0
    for content in contents:
      if (i == 0):
        user_name = content
        i = i + 1
      else:
        user_about = content
    await client(UpdateProfileRequest(first_name=user_name, about=user_about))
    await client(
      UploadProfilePhotoRequest(await
                                client.upload_file(me.username + '.jpg')))
    f.close()
    await event.edit("i tuoi dati sono stati copiati con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'ghostreset'))
async def handler(event):
  global me
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    f = open("info_tot.txt", "r", encoding="utf-8")
    contents = f.readlines()
    i = 0
    for content in contents:
      if (i == 0):
        user_name = content
        i = i + 1
      else:
        user_about = content
    await client(UpdateProfileRequest(first_name=user_name, about=user_about))
    await client(
      UploadProfilePhotoRequest(await
                                client.upload_file(me.username + '.jpg')))
    f.close()
    await event.edit("i tuoi dati sono stati copiati con successo!")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'allora'))
async def handler(event):
  await event.edit("""allora
    
o""")
  await event.edit("""allora
    
or""")
  await event.edit("""allora
    
ora""")
  await event.edit("""allora
    
orat""")
  await event.edit("""allora
    
orati""")
  await event.edit("""allora
    
oratic""")
  await event.edit("""allora
    
oratica""")
  await event.edit("""allora
    
oraticam""")
  await event.edit("""allora
    
oraticame""")
  await event.edit("""allora
    
oraticamen""")
  await event.edit("""allora
    
oraticament""")
  await event.edit("""allora
    
oraticamentw""")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'putin'))
async def handler(event):
  await event.edit("""⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿
⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿
⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿
⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿
⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿
⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿
⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿
⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿
⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉
⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄""")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'kim'))
async def handler(event):
  await event.edit("""⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿ 
⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿ 
⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿ 
⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻ 
⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄ 
⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄
""")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'trump'))
async def handler(event):
  await event.edit("""⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿
⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿
⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿
⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿
⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿
⡿⠟⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠉⠛⠿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠄⠄⠈⠹
⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠄""")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'obama'))
async def handler(event):
  await event.edit("""
░░█▀░░░░░░░░░░░▀▀███████░░░░░
░░█▌░░░░░░░░░░░░░░░▀██████░░░
░█▌░░░░░░░░░░░░░░░░███████▌░░
░█░░░░░░░░░░░░░░░░░████████░░
▐▌░░░░░░░░░░░░░░░░░▀██████▌░░
░▌▄███▌░░░░▀████▄░░░░▀████▌░░
▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░
▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌
▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌
▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌
░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░
░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░
░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░
░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░
░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░
░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░
░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░
░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░
░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░
▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░
     """)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'cascata'))
async def handler(event):
  global punto, spazio
  global casca
  cascat = casca
  for i in range(2):
    for i in range(10):
      for x in range(i):
        cascat += spazio
      cascat += punto
      cascat += '\r\n'
      await event.edit(cascat)
    for i in range(10, -1, -1):
      for x in range(i):
        cascat += spazio
      cascat += punto
      cascat += '\r\n'
      await event.edit(cascat)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'pisnelo'))
async def handler(event):
  global otto, duepunti
  pipo = []
  pipo.append(otto)
  await event.edit(pipo)
  for i in range(10):
    pipo.append(duepunti)
    await event.edit(pipo)
  pipo.append("D")
  await event.edit(pipo)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'mp3'))
async def handler(event):
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)
  if (sender_main.username == me.username):
    message = await event.get_reply_message()
    file_exists = exists('voice.mp3')
    if (file_exists):
      os.remove('voice.mp3')
    file_exists = exists('converted.mp3')
    if (file_exists):
      os.remove('converted.mp3')
    path = await message.download_media()
    print(message)
    print(path)
    # convert mp3 file to wav
    src = str(path)
    print(src)
    dst = "converted.mp3"
    try:
      sound = AudioSegment.from_ogg(src)
    except Exception as e:
      print(e)

    sound.export(dst, format="mp3")
    await client.send_file(message_main.peer_id,
                           'converted.mp3',
                           voice_note=False)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'tras'))
async def handler(event):
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    message = await event.get_reply_message()
    file_exists = exists('voice.mp3')
    if (file_exists):
      os.remove('voice.mp3')
    path = await message.download_media()
    print(message)
    print(path)
    # convert mp3 file to wav
    src = str(path)  #str(user_path) + "\\"+str(path)
    print(src)
    dst = "trs.wav"

    try:
      sound = AudioSegment.from_mp3(src)
      sound.export(dst, format="wav")
    except Exception as e:
      print(e)

    try:
      sound = AudioSegment.from_ogg(src)
      sound.export(dst, format="wav")
    except Exception as e:
      print(e)

    file_audio = sr.AudioFile("trs.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with file_audio as source:
      audio_text = r.record(source)

    await event.edit(r.recognize_google(audio_text, language="it-IT"))


@client.on(events.NewMessage(pattern='(?i)' + cm + 'trit'))
async def handler(event):
  message_main = event.message
  message = await event.get_reply_message()
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    translator = gtn.google_translator()
    translation = translator.translate(message.text, lang_tgt='it-IT')
    await event.edit(translation)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'tren'))
async def handler(event):
  message_main = event.message
  message = await event.get_reply_message()
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    translator = gtn.google_translator()
    translation = translator.translate(message.text, lang_tgt='en-EN')
    await event.edit(translation)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'speak'))
async def handler(event):
  global language
  me = await client.get_me()
  message = await event.get_reply_message()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    myobj = gTTS(text=message.text, lang=language, slow=False)
    myobj.save("voice.mp3")
    await client.send_file(message_main.peer_id, 'voice.mp3', voice_note=True)


@client.on(events.NewMessage(pattern='(?i)' + cm + 'foto persona'))
async def handler(event):
  me = await client.get_me()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    image_url = "https://thispersondoesnotexist.com/image"
    img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler_:
      handler_.write(img_data)
    await client.send_file(event.message.chat_id, "image_name.jpg")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'foto anime'))
async def handler(event):
  me = await client.get_me()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  rnd = random.randint(1, 100000)

  if (sender_main.username == me.username):
    image_url = "https://www.thiswaifudoesnotexist.net/example-" + str(
      rnd) + ".jpg"
    img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler_:
      handler_.write(img_data)
    await client.send_file(event.message.chat_id, "image_name.jpg")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'foto gatto'))
async def handler(event):
  me = await client.get_me()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    image_url = "https://thiscatdoesnotexist.com/"
    img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler_:
      handler_.write(img_data)
    await client.send_file(event.message.chat_id, "image_name.jpg")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'dona'))
async def handler(event):
  me = await client.get_me()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    await event.edit("Supporta il creatore: https://paypal.me/mastertiger8")


@client.on(events.NewMessage(pattern='(?i)' + cm + 'donazione'))
async def handler(event):
  me = await client.get_me()
  message_main = event.message
  if (message_main.from_id == None):
    sender_main = await client.get_entity(message_main.peer_id)
  else:
    sender_main = await client.get_entity(message_main.from_id)

  if (sender_main.username == me.username):
    await event.edit("Supporta il creatore: https://paypal.me/mastertiger8")


client.run_until_disconnected()
