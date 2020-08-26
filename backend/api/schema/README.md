# Schema Notes

Should be noted that created_at is a str instead of a date and time. I only
did this because I don't know how to use datetime with marshmallow
not sure how to use marshmallow for constraints i.e. EntrySchema->author is
just a string NOT a user