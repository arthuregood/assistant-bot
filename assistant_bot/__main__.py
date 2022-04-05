import pymysql.cursors
import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = 'insert token here'
bot = telegram.Bot(token=token)

connection = pymysql.connect(host='localhost',
                             user='arthur',
                             password='root',
                             database='assistant_db',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    cursor.execute("SHOW DATABASES LIKE 'assistant_db'")


def start(update, context):
    user = update.effective_user
    print(user)
    """ update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    ) """
    # print welcome message

# update.message.reply_text()


def bot_help(update, context):
    pass


def listen_message(update, context):
    received_message = update.message.text
    user = update.effective_user

    if '-' in received_message:
        save_message(received_message, user)
        return

    elif 'delete' in received_message:
        delete_message(received_message, user)
        return

    list_messages(received_message, user)
    return


def save_message(message, user):
    for bar in [' - ', ' -', '- ']:
        message = message.replace(bar, '-', 1)

    message_type, description = message.split('-', 1)
    print(message_type, description)

    sql = """
        CREATE TABLE IF NOT EXISTS message_register (
        id int NOT NULL AUTO_INCREMENT,
        user_id double NOT NULL,
        type VARCHAR(30) NOT NULL,
        message VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    );"""

    with connection.cursor() as cursor:
      cursor.execute(sql)

      sql = f"""INSERT INTO message_register ({int(user.id)}, {message_type}, {description}) """

      cursor.execute(sql)


def list_messages(message):
    pass


def delete_message(message):
    pass


def main():
    updater = Updater(
        token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(MessageHandler(Filters.text & ~
                   Filters.command, listen_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
