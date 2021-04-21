CREATE TABLE IF NOT EXISTS activity (
    activityId integer PRIMARY KEY,
    activityName text,
    activityDetail text,
    timestamp text
)

CREATE TABLE IF NOT EXISTS jurnal(
        moodId integer PRIMARY KEY,
        date text,
        mood_record text,
        notes text
) 

CREATE TABLE IF NOT EXISTS roomchat(
        chatId, integer PRIMARY KEY,
        firstUserId integer,
        mood_record text,
        notes text
) 