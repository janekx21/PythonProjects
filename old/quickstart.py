import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
json_key = json.load(open('client_secret_1033617619515-93p0cc389fnvtn67peioa22r8gq9d5vb.apps.googleusercontent.com.json'))

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_id.json', scope)


gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Where is the money Lebowski?").sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A1:B7')
