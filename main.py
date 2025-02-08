import uuid

from pyrogram import Client, filters
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    BOT_USERNAME
)

bot = Client(
    "bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot_username = BOT_USERNAME

messages = {}

@bot.on_message(filters.command(["start"], prefixes=["/", "."]))
async def start(client, message: Message):
    full_name = message.from_user.first_name
    if message.from_user.last_name:
        full_name += f" {message.from_user.last_name}"
    
    welcome_text = (
        f"👋 **Welcome, {full_name}!**\n\n"
        "🌐 **I'm the Whisper Bot.**\n\n"
        "💬 You can use me to send secret whispers in groups.\n\n"
        "🔮 I work in the Inline mode, which means you can use me even if I'm not in the group.\n\n"
        "💌 It's very easy to use me. Simply forward a message from a user to whom you want to send a whisper, and I'll do the rest for you.\n\n"
        "There are other ways to use me too. If you are interested in learning more about me, click on the **Help** button."
    )
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Update Channel", url="https://t.me/ModVipRM"), InlineKeyboardButton("My Dev 👨‍💻", user_id=7303810912)],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ])
    
    await message.reply_text(welcome_text, reply_markup=buttons)

@bot.on_callback_query(filters.regex("help"))
async def help_callback(client, callback_query):
    help_text = (
        "The other way to use me is to write the inline query by yourself.\n\n"
        "The format should be in this arrangement:\n\n"
        "`@CcZxdvvtfBot your whisper @username`\n\n"
        "Now I'll split the format into 3 parts and explain each part of it:\n\n"
        "1. `@CcZxdvvtfBot`:\n"
        "   This is my username; it should be at the beginning of the inline query so I'll know that you are using me and not another bot.\n\n"
        "2. `whisper message`:\n"
        "   This is the whisper that will be sent to the target user. Replace `your whisper` with your actual message.\n\n"
        "3. `@username`:\n"
        "   You should replace this with the target's username so the bot will know which user should receive your whisper message.\n\n"
        "**Example:**\n"
        "`@CcZxdvvtfBot hello this is a test @abirxdhackz`\n\n"
        "📎 The bot works in groups and the target user should be in the same group as you.\n\n"
        "What are you waiting for?! **Try me now 😉**"
    )
    back_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
    ])
    
    await callback_query.message.edit_text(help_text, reply_markup=back_button)

@bot.on_callback_query(filters.regex("back"))
async def back_callback(client, callback_query):
    full_name = callback_query.from_user.first_name
    if callback_query.from_user.last_name:
        full_name += f" {callback_query.from_user.last_name}"

    welcome_text = (
        f"👋 **Welcome, {full_name}!**\n\n"
        "🌐 **I'm the Whisper Bot.**\n\n"
        "💬 You can use me to send secret whispers in groups.\n\n"
        "🔮 I work in the Inline mode, which means you can use me even if I'm not in the group.\n\n"
        "💌 It's very easy to use me. Simply forward a message from a user to whom you want to send a whisper, and I'll do the rest for you.\n\n"
        "There are other ways to use me too. If you are interested in learning more about me, click on the **Help** button."
    )
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Update Channel", url="https://t.me/ModVipRM"), InlineKeyboardButton("My Dev 👨‍💻", user_id=7303810912)],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ])
    
    await callback_query.message.edit_text(welcome_text, reply_markup=buttons)

@bot.on_inline_query()
async def answer(client, inline_query):
    text = inline_query.query.strip()

    print(f"Inline query received: '{text}'")

    if not text or len(text.split()) < 2:
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="How to Send Secret Message",
                    description="Include the recipient's @username or user ID at the end of your message.",
                    input_message_content=InputTextMessageContent(
                        "How to Send Secret Message\n\n"
                        "Include the recipient's @username or user ID at the end of your message.\n\n"
                        "**Example:** @CcZxdvvtfBot Hello there! @username"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Start Bot", url=f"https://t.me/{bot_username}?start=inline_help")]]
                    )
                )
            ],
            cache_time=1
        )
        return

    parts = text.split()
    recipient_identifier = parts[-1]
    message_content = " ".join(parts[:-1])
    message_id = str(uuid.uuid4())

    recipient_id = None
    recipient_username = None
    full_name = "the recipient"

    if recipient_identifier.startswith("@"):
        recipient_username = recipient_identifier[1:]
        try:
            recipient_user = await client.get_users(recipient_username)
            recipient_id = recipient_user.id
            full_name = recipient_user.first_name
            if recipient_user.last_name:
                full_name += f" {recipient_user.last_name}"
        except Exception as e:
            print(f"Error fetching recipient user by username: {str(e)}")
            await inline_query.answer(
                results=[
                    InlineQueryResultArticle(
                        id=str(uuid.uuid4()),
                        title="Recipient Not Found",
                        description="Recipient not found. Please try again with a valid username.",
                        input_message_content=InputTextMessageContent("Recipient not found. Please try again with a valid username."),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Learn More", url=f"https://t.me/{bot_username}?start=inline_help")]]
                        )
                    )
                ],
                cache_time=1
            )
            return
    elif recipient_identifier.isdigit():
        try:
            recipient_id = int(recipient_identifier)
            recipient_user = await client.get_users(recipient_id)
            full_name = recipient_user.first_name
            if recipient_user.last_name:
                full_name += f" {recipient_user.last_name}"
        except Exception as e:
            print(f"Error fetching recipient user by ID: {str(e)}")
            await inline_query.answer(
                results=[
                    InlineQueryResultArticle(
                        id=str(uuid.uuid4()),
                        title="Ask Recipient to Start the Bot",
                        description="Recipient not found. Ask the recipient to start the bot first.",
                        input_message_content=InputTextMessageContent(
                            "The recipient is not found. Please ask the recipient to start the bot first, and then you can send secret messages."
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Start Bot", url=f"https://t.me/{bot_username}?start=inline_help")]]
                        )
                    )
                ],
                cache_time=1
            )
            return
    else:
        print(f"Invalid recipient identifier: '{recipient_identifier}'")
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="How to Send Secret Message",
                    description="Include the recipient's @username or user ID at the end of your message.",
                    input_message_content=InputTextMessageContent(
                        "How to Send Secret Message\n\n"
                        "Include the recipient's @username or user ID at the end of your message.\n\n"
                        "**Example:** @CcZxdvvtfBot Hello there! @username"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Start Bot", url=f"https://t.me/{bot_username}?start=inline_help")]]
                    )
                )
            ],
            cache_time=1
        )
        return

    messages[message_id] = {
        "content": message_content,
        "sender_id": inline_query.from_user.id,
        "recipient_id": recipient_id
    }

    print(f"Message Stored: ID={message_id}, Content='{message_content}'")

    whisper_message = f"🔒 **Whisper to {full_name}**, only viewable by you and them."
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=f"Send a Whisper Message to {full_name}",
            description="he/she can open it",
            input_message_content=InputTextMessageContent(whisper_message),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("👀 Show Message 🔒", callback_data=message_id)]
            ])
        )
    ]
    
    print(f"Sending inline query result: '{whisper_message}'")

    await inline_query.answer(results, cache_time=1)

@bot.on_callback_query(filters.create(lambda _, __, query: query.data in messages))
async def whisper_callback(client, callback_query):
    message_id = callback_query.data
    user_id = callback_query.from_user.id
    message_data = messages.get(message_id)

    if not message_data:
        await callback_query.answer("Message not found or expired.", show_alert=True)
        return

    sender_id = message_data["sender_id"]
    recipient_id = message_data["recipient_id"]

    if user_id == sender_id or user_id == recipient_id:
        message_content = message_data["content"]
        try:
            await callback_query.answer(f"{message_content}", show_alert=True)
            print(f"Response Sent: {message_content}")
        except Exception as e:
            print(f"Error in responding: {str(e)}")
    else:
        await callback_query.answer("❌ Hey Dear! This message is not for you.", show_alert=True)

bot.run()