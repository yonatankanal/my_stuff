import pandas as pd
import win32com.client as win32



def main():
    make_data()
    

def make_data():
    file_one_path = "sample_files/spreadsheet_1.xlsx"
    file_two_path = 'sample_files/spreadsheet_2.xlsx'
    df_1 = pd.read_excel(file_one_path)
    df_cleaned_1 = df_1.dropna(subset=['Dates'])
    df_2 = pd.read_excel(file_two_path)
    df_cleaned_2 = df_2.dropna(subset=['Dates'])

    all_the_data = pd.merge(df_cleaned_1, df_cleaned_2, on=['First Name', 'Last Name'], how='inner')
    print (all_the_data)

    for index, row in all_the_data.iterrows():
        name = row['First Name']
        current = row['Practice Setting_x']
        future = row['Practice Setting_y']

        create_email(name,current,future)


def create_email(name,current,future):
    body = f'''

    Dear {name},

    Congratulations on completing your first Level II Fieldwork at {current}! You made it! Although it may seem like you are starting 
    over in some capacity at the {future}, remember that you have even more knowledge than you had 3 months ago. You’ve got this!

    I hope this week goes well—please let me know how things are going. Remember that you can always reach out to myself or Ann with any questions or concerns.

    Take care,
    Avital

    '''

    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = "recipient"
    mail.Subject = "subject"
    mail.Body = body
    mail.Display(True)



if __name__ == "__main__":
    main()