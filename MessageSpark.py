from ciscosparkapi import CiscoSparkAPI

my_token   = "MjE2NzMzZGItY2UzYi00ODlhLWI0NWItMTg3ZjdlZDg2ZWVhNzUzNzFmYzctNzc3"
bot_token  = "MjFlZGFlMzQtYzA5OC00NTc4LTgxMzgtNGM1ZGM4OTQ1NGNkNjYwNjFhN2ItNTk2"
SPARK_ROOM_NAME = "FabriRoom"
SPARK_ROOM_ID = "Y2lzY29zcGFyazovL3VzL1JPT00vMzQzODRhMTAtMWE4Yi0xMWU3LTlmNzAtMzE5ZjUxNDkyOWNm"
SPARK_MESSAGE = u"Cisco Spark rocks!  \ud83d\ude0e"
SPARK_FILE_URL = "https://developer.ciscospark.com/images/logo_spark_lg@256.png"

# Send a test messgae using my Spark token
my_api = CiscoSparkAPI(my_token)
my_api.messages.create(SPARK_ROOM_ID, text=SPARK_MESSAGE)

# Send a file using bot Spark token
bot_api = CiscoSparkAPI(bot_token)
bot_api.messages.create(SPARK_ROOM_ID, files=[SPARK_FILE_URL])
