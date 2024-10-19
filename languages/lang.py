import csv

languages = ['English', 'Welsh or Cymraeg', 'Gaelic (Irish)', 'Gaelic (Scottish)', 'Manx Gaelic', 'Gaelic (Not otherwise specified)', 'Cornish', 'Scots', 'Ulster Scots', 'Romany English', 'Irish Traveller Cant', 'French', 'Portuguese', 'Spanish', 'Italian', 'German', 'Polish', 'Slovak', 'Czech', 'Romanian', 'Lithuanian', 'Latvian', 'Hungarian', 'Bulgarian', 'Greek', 'Dutch', 'Swedish', 'Danish', 'Finnish', 'Estonian', 'Slovenian', 'Maltese', 'Any other European language (EU)', 'Albanian', 'Ukrainian', 'Any other Eastern European language (non EU)', 'Northern European language (non EU)', 'Bosnian, Croatian, Serbian, Montenegrin', 'Any Romani language', 'Yiddish', 'Russian', 'Turkish', 'Arabic', 'Hebrew', 'Kurdish', 'Persian or Farsi', 'Pashto', 'Any other West or Central Asian language', 'Urdu', 'Hindi', 'Panjabi', 'Pakistani Pahari (with Mirpuri and Potwari)', 'Bengali (with Sylheti and Chatgaya)', 'Gujarati', 'Marathi', 'Telugu', 'Tamil', 'Malayalam', 'Sinhala', 'Nepalese', 'Any other South Asian language', 'Mandarin Chinese', 'Cantonese Chinese', 'All other Chinese', 'Japanese', 'Korean', 'Vietnamese', 'Thai', 'Malay', 'Tagalog or Filipino', 'Any other East Asian language', 'Oceanic or Australian language', 'North or South American language', 'English-based Caribbean Creole', 'Any other Caribbean Creole', 'Amharic', 'Tigrinya', 'Somali', 'Krio', 'Akan', 'Yoruba', 'Igbo', 'Swahili or Kiswahili', 'Luganda', 'Lingala', 'Shona', 'Afrikaans', 'Any other Nigerian language', 'Any other West African language', 'Any other African language', 'British Sign Language', 'Any other sign language', 'Any sign communication system', 'Other language']

def getboroughbylang (language):
    boroughswithlang = []
    with open('newlangcensus.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[2] == (str(languages.index(language)+1)):
                print('hi')
                boroughswithlang.append([int(row[4]), row[1]])
    boroughswithlang.sort(key=lambda x: x[0], reverse=True)
    return boroughswithlang

def oatoborough(oa):
    with open('summary.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == oa:
                return row[2]

def boroughtooas(borough):
    oas = []
    with open('summary.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[2] == borough:
                oas.append(row[0])
    return oas
