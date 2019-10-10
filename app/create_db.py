#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('/app/sessions.db')
conn.execute('CREATE TABLE students (id VARCHAR(256), p1line VARCHAR(256), p1val VARCHAR(256), p2col VARCHAR(256), p2val VARCHAR(256))')
conn.close()
