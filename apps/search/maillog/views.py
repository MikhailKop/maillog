from datetime import datetime

import django.shortcuts
from django.db import connection
from django.http import JsonResponse


def search(request):
    if request.method != "POST":
        return django.shortcuts.render(request, "search.html")
    address = request.POST.get("address")

    textSql = f"SELECT * FROM \
        (SELECT message.int_id as id, message.created AS created, message.str \
        FROM message \
        INNER JOIN \
        (SELECT log.int_id as at_id, log.created, log.str \
        FROM log \
        WHERE log.address = '{address}') \
        ON at_id = message.int_id \
        UNION ALL SELECT log.int_id AS id, log.created AS created, log.str \
        FROM log WHERE log.address = '{address}') ORDER BY id, created ASC;"

    records = []
    with connection.cursor() as cursor:
        cursor.execute(textSql)
        rows = cursor.fetchall()

        """converting date fields for successful serialization to JSON"""
        for row in rows:
            record = {}
            for i, column in enumerate(cursor.description):
                record[column.name] = row[i]
                if type(row[i]) is datetime:
                    record[column.name] = row[i].strftime("%Y-%m-%d %H:%M:%S")

            records.append(record)
    return JsonResponse(records, safe=False)
