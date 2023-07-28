import csv
import pandas as pd
import matplotlib.pyplot as plt
import customtkinter 
import tkinter as tk
from tkinter import messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



# Import CSV file(s)
pff2022 = "PFF2022.csv"
pff2021 = "PFF2021.csv"
pff2020 = "PFF2020.csv"
pff2019 = "PFF2019.csv"
pff2018 = "PFF2018.csv"

# Open CSV file and read data (2018-2022)
with open(pff2022, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row
    data = []

        # Loop through data
    for row in reader:
        name = row[0].strip()
        AccPercentString = row[5].strip()  # Remove leading and trailing spaces

        if AccPercentString:  # Check if the string is non-empty
            try:
                AccPercentFloat = float(AccPercentString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                error = True
        else:
            error = True
        BigTimeThrows = int(row[11])
        bigtimerate = float(row[12])
        AvgTimeTThrow = float(row[9])
        Dropbacks = int(row[18])
        OffenseGrade = float(row[23])
        PassGrade = float(row[24])
        RushGradeString = row[25].strip()
        if RushGradeString:  # Check if the string is non-empty
            try:
                RushGradeFloat = float(RushGradeString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:   
                error = True  
        else:
            error = True
            

        TurnOverWorthyPlays = int(row[38])
        TWPrate = float(row[39])
        yards = int(row[40])
        ypa = float(row[41])
        year = int(row[42])

        #Validate data for min. number of dropbacks
        if Dropbacks >= 10:
            data.append([name, AccPercentFloat, BigTimeThrows, bigtimerate, AvgTimeTThrow, Dropbacks, OffenseGrade, PassGrade, RushGradeFloat, TurnOverWorthyPlays, TWPrate, yards, ypa, year])
#Add 2021 Data
with open(pff2021, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row

        # Loop through data
    for row in reader:
        name = row[0]
        AccPercentString = row[5].strip()  # Remove leading and trailing spaces

        if AccPercentString:  # Check if the string is non-empty
            try:
                AccPercentFloat = float(AccPercentString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                error = True
        else:
            error = True
        BigTimeThrows = int(row[11])
        bigtimerate = float(row[12])
        AvgTimeTThrow = float(row[9])
        Dropbacks = int(row[18])
        OffenseGrade = float(row[23])
        PassGrade = float(row[24])
        RushGradeString = row[25].strip()
        if RushGradeString:  # Check if the string is non-empty
            try:
                RushGradeFloat = float(RushGradeString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:   
                error = True  
        else:
            error = True
            

        TurnOverWorthyPlays = int(row[38])
        TWPrate = float(row[39])
        yards = int(row[40])
        ypa = float(row[41])
        year = int(row[42])

        #Validate data for min. number of dropbacks
        if Dropbacks >= 10:
            data.append([name, AccPercentFloat, BigTimeThrows, bigtimerate, AvgTimeTThrow, Dropbacks, OffenseGrade, PassGrade, RushGradeFloat, TurnOverWorthyPlays, TWPrate, yards, ypa, year])
#Add 2020 Data
with open(pff2020, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row

        # Loop through data
    for row in reader:
        name = row[0]
        AccPercentString = row[5].strip()  # Remove leading and trailing spaces

        if AccPercentString:  # Check if the string is non-empty
            try:
                AccPercentFloat = float(AccPercentString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")
        BigTimeThrows = int(row[11])
        bigtimerate = float(row[12])
        AvgTimeTThrow = float(row[9])
        Dropbacks = int(row[18])
        OffenseGrade = float(row[23])
        PassGrade = float(row[24])
        RushGradeString = row[25].strip()
        if RushGradeString:  # Check if the string is non-empty
            try:
                RushGradeFloat = float(RushGradeString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")

        TurnOverWorthyPlays = int(row[38])
        TWPrate = float(row[39])
        yards = int(row[40])
        ypa = float(row[41])
        year = int(row[42])

        #Validate data for min. number of dropbacks
        if Dropbacks >= 10:
            data.append([name, AccPercentFloat, BigTimeThrows, bigtimerate, AvgTimeTThrow, Dropbacks, OffenseGrade, PassGrade, RushGradeFloat, TurnOverWorthyPlays, TWPrate, yards, ypa, year])   
#Add 2019 Data
with open(pff2019, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row

        # Loop through data
    for row in reader:
        name = row[0]
        AccPercentString = row[5].strip()  # Remove leading and trailing spaces

        if AccPercentString:  # Check if the string is non-empty
            try:
                AccPercentFloat = float(AccPercentString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")
        BigTimeThrows = int(row[11])
        bigtimerate = float(row[12])
        AvgTimeTThrow = float(row[9])
        Dropbacks = int(row[18])
        OffenseGrade = float(row[23])
        PassGrade = float(row[24])
        RushGradeString = row[25].strip()
        if RushGradeString:  # Check if the string is non-empty
            try:
                RushGradeFloat = float(RushGradeString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")

        TurnOverWorthyPlays = int(row[38])
        TWPrate = float(row[39])
        yards = int(row[40])
        ypa = float(row[41])
        year = int(row[42])

        #Validate data for min. number of dropbacks
        if Dropbacks >= 10:
            data.append([name, AccPercentFloat, BigTimeThrows, bigtimerate, AvgTimeTThrow, Dropbacks, OffenseGrade, PassGrade, RushGradeFloat, TurnOverWorthyPlays, TWPrate, yards, ypa, year])
#Add 2018 Data
with open(pff2018, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row

        # Loop through data
    for row in reader:
        name = row[0]
        AccPercentString = row[5].strip()  # Remove leading and trailing spaces

        if AccPercentString:  # Check if the string is non-empty
            try:
                AccPercentFloat = float(AccPercentString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")
        BigTimeThrows = int(row[11])
        bigtimerate = float(row[12])
        AvgTimeTThrow = float(row[9])
        Dropbacks = int(row[18])
        OffenseGrade = float(row[23])
        PassGrade = float(row[24])
        RushGradeString = row[25].strip()
        if RushGradeString:  # Check if the string is non-empty
            try:
                RushGradeFloat = float(RushGradeString.replace("'", ""))
            # Process AccPercentFloat as needed
            except ValueError:
                print("")
        else:
            print("")

        TurnOverWorthyPlays = int(row[38])
        TWPrate = float(row[39])
        yards = int(row[40])
        ypa = float(row[41])
        year = int(row[42])

        #Validate data for min. number of dropbacks
        if Dropbacks >= 10:
            data.append([name, AccPercentFloat, BigTimeThrows, bigtimerate, AvgTimeTThrow, Dropbacks, OffenseGrade, PassGrade, RushGradeFloat, TurnOverWorthyPlays, TWPrate, yards, ypa, year])


#set name list for combo box            
all_names = []
uniquie_names = []
for i in range(-1, len(data)):
    all_names.append(data[i][0])
#get rid of duplicates
unique_names = []
for name in all_names:
    if name not in unique_names:
        unique_names.append(name)
#sort the names in alphabetical order
unique_names = sorted(unique_names)



#Build GUI framework
class playerPlotter(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('NFL QB Player Plotter')
        self.geometry(f"{1200}x{700}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=215, corner_radius=10, fg_color='#dfb973')
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=0)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="NFL Player Plotter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="center")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(190, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="center")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 0))
        
        #User Name Input
        self.player1_label = customtkinter.CTkLabel(self.sidebar_frame, text="Player 1:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.player1_label.grid(row=1, column=0, padx=20, pady=10)
        self.player1_combobox1 = customtkinter.CTkComboBox(self.sidebar_frame, values=unique_names, width=150)
        self.player1_combobox1.grid(row=1, column=1, padx=5, pady=10)  
        self.player1_combobox1.bind('<KeyRelease>',self.create_plot)
        self.player2_label = customtkinter.CTkLabel(self.sidebar_frame, text="Player 2:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.player2_label.grid(row=2, column=0, padx=20, pady=10)
        self.player2_combobox2 = customtkinter.CTkComboBox(self.sidebar_frame, values=unique_names, width=150)
        self.player2_combobox2.grid(row=2, column=1, padx=5, pady=30)
        self.player2_combobox2.bind('<KeyRelease>', self.create_plot)

        #x & y statistic
        self.xstat_label = customtkinter.CTkLabel(self.sidebar_frame, text="x axis statistic:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.xstat_label.grid(row=3, column=0, padx=5, pady=(5,5))
        self.xcombobox = customtkinter.CTkComboBox(self.sidebar_frame,values=['Accuracy', 'Big Time Throws', 'Big Time Throw Rate', 'Avg. Time To Throw', 'Dropbacks', 'Offense Grade', 'Pass Grade', 'Rush Grade', 'Turn Over Worthy Plays', 'Turnover Worthy Play Rate', 'Yards', 'Yard/Attempt'])
        self.xcombobox.grid(row=3, column=1, padx=(0,10), pady=(5, 5))
        self.xcombobox.set("X-Statistic")
        self.xcombobox.bind('<KeyRelease>')

        self.ystat_label = customtkinter.CTkLabel(self.sidebar_frame, text="y axis statistic:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.ystat_label.grid(row=4, column=0, padx=5, pady=(5,5))
        self.ycombobox = customtkinter.CTkComboBox(self.sidebar_frame,values=['Accuracy', 'Big Time Throws', 'Big Time Throw Rate', 'Avg. Time To Throw', 'Dropbacks', 'Offense Grade', 'Pass Grade', 'Rush Grade', 'Turn Over Worthy Plays', 'Turnover Worthy Play Rate', 'Yards', 'Yard/Attempt'])
        self.ycombobox.grid(row=4, column=1, padx=(0,10), pady=(5,5))
        self.ycombobox.set("Y-Statistic")
        self.ycombobox.bind('<KeyRelease>')

        #Create Plot Button
        self.plot_button = customtkinter.CTkButton(self.sidebar_frame, text= 'Create Plot', command=self.create_plot)        
        self.plot_button.grid(row=5, column=0, padx=20, pady=10)

        #create plot frame
        self.plot_frame = customtkinter.CTkFrame(self, width=250, corner_radius= 10)
        self.plot_frame.grid(row=0, column=1, rowspan=5, padx=(0, 0), pady=(0, 0), sticky="nsew")
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def create_plot(self):
        xstat_player1 = []
        ystat_player1 = []
        xstat_player2 = []
        ystat_player2 = []
        year_player1_x = []
        year_player1_y = []
        year_player2_x = []
        year_player2_y = []
        player1 = self.player1_combobox1.get()
        player2 = self.player2_combobox2.get()
        xstat = self.xcombobox.get()
        ystat = self.ycombobox.get()
        messagebox.showinfo("Creating Plot...",f'Creating Plot for {player1} and {player2} using {xstat} as x-axis and {ystat} as y-axis.')
        #Gather players  X-statistic from year
        for i in range(-1,len(data)):
            if player1 == data[i][0]:
                if xstat == 'Accuracy':
                    xstat_player1.append(data[i][1])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Big Time Throws':
                    xstat_player1.append(data[i][2])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Big Time Throw Rate':
                    xstat_player1.append(data[i][3])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Avg. Time To Throw':
                    xstat_player1.append(data[i][4])
                    year_player1_x.append(data[i][13])                
                elif xstat == 'Dropbacks':
                    xstat_player1.append(data[i][5])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Offense Grade':
                    xstat_player1.append(data[i][6])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Pass Grade':
                    xstat_player1.append(data[i][7])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Rush Grade':
                    xstat_player1.append(data[i][8])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Turn Over Worthy Plays':
                    xstat_player1.append(data[i][9])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Turn Over Worthy Plays Rate':
                    xstat_player1.append(data[i][10])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Yards':
                    xstat_player1.append(data[i][11])
                    year_player1_x.append(data[i][13])
                elif xstat == 'Yards/Attempt':
                    xstat_player1.append(data[i][12])
                    year_player1_x.append(data[i][13])
                messagebox.showinfo("Plot Data",f'{player1} {xstat}: {xstat_player1}  {year_player1_x}')
        
        #Same For Player2             
        for i in range(-1,len(data)):
            if player2 == data[i][0]:
                if xstat == 'Accuracy':
                    xstat_player2.append(data[i][1])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Big Time Throws':
                    xstat_player2.append(data[i][2])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Big Time Throw Rate':
                    xstat_player2.append(data[i][3])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Avg. Time To Throw':
                    xstat_player2.append(data[i][4])
                    year_player2_x.append(data[i][13])                
                elif xstat == 'Dropbacks':
                    xstat_player2.append(data[i][5])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Offense Grade':
                    xstat_player2.append(data[i][6])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Pass Grade':
                    xstat_player2.append(data[i][7])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Rush Grade':
                    xstat_player2.append(data[i][8])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Turn Over Worthy Plays':
                    xstat_player2.append(data[i][9])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Turn Over Worthy Plays Rate':
                    xstat_player2.append(data[i][10])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Yards':
                    xstat_player2.append(data[i][11])
                    year_player2_x.append(data[i][13])
                elif xstat == 'Yards/Attempt':
                    xstat_player2.append(data[i][12])
                    year_player2_x.append(data[i][13])
                messagebox.showinfo("Plot Data",f'{player2} {xstat}: {xstat_player2}  {year_player2_x}')    
        #Now for Y-statistic
        for i in range(-1,len(data)):
            if player1 == data[i][0]:
                if ystat == 'Accuracy':
                    ystat_player1.append(data[i][1])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Big Time Throws':
                    ystat_player1.append(data[i][2])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Big Time Throw Rate':
                    ystat_player1.append(data[i][3])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Avg. Time To Throw':
                    ystat_player1.append(data[i][4])
                    year_player1_y.append(data[i][13])                
                elif ystat == 'Dropbacks':
                    ystat_player1.append(data[i][5])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Offense Grade':
                    ystat_player1.append(data[i][6])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Pass Grade':
                    ystat_player1.append(data[i][7])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Rush Grade':
                    ystat_player1.append(data[i][8])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Turn Over Worthy Plays':
                    ystat_player1.append(data[i][9])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Turn Over Worthy Plays Rate':
                    ystat_player1.append(data[i][10])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Yards':
                    ystat_player1.append(data[i][11])
                    year_player1_y.append(data[i][13])
                elif ystat == 'Yards/Attempt':
                    ystat_player1.append(data[i][12])
                    year_player1_y.append(data[i][13])
                messagebox.showinfo("Plot Data",f'{player1} {ystat}: {ystat_player1}  {year_player1_y}')  

        for i in range(-1,len(data)):
            if player2 == data[i][0]:
                if ystat == 'Accuracy':
                    ystat_player2.append(data[i][1])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Big Time Throws':
                    ystat_player2.append(data[i][2])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Big Time Throw Rate':
                    ystat_player2.append(data[i][3])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Avg. Time To Throw':
                    ystat_player2.append(data[i][4])
                    year_player2_y.append(data[i][13])                
                elif ystat == 'Dropbacks':
                    ystat_player2.append(data[i][5])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Offense Grade':
                    ystat_player2.append(data[i][6])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Pass Grade':
                    ystat_player2.append(data[i][7])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Rush Grade':
                    ystat_player2.append(data[i][8])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Turn Over Worthy Plays':
                    ystat_player2.append(data[i][9])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Turn Over Worthy Plays Rate':
                    ystat_player2.append(data[i][10])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Yards':
                    ystat_player2.append(data[i][11])
                    year_player2_y.append(data[i][13])
                elif ystat == 'Yards/Attempt':
                    ystat_player2.append(data[i][12])
                    year_player2_y.append(data[i][13])
                messagebox.showinfo("Plot Data",f'{player2} {ystat}: {xstat_player2}  {year_player2_y}')               
                    
'''
        xy_player1 = pd.DataFrame({'name': name, 'x': x, 'y': y})
        xy_player2 = pd.DataFrame({'name': name, 'x': x, 'y': y})

        # Find grade averages for pressured and un-pressured league-wide
        #clean_avg = xy['x'].mean()
        #pressure_avg = xy['y'].mean()

        #Define the plot
        fig, ax = plt.subplots()

        ax.scatter(xy_player1['x'], xy_player1['y'], s=20, c='red')

        # Move left y-axis and bottom x-axis to center, passing through (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # Set x and y axis limits
        plt.xlim((40, 100))
        plt.ylim((20, 100))

        # Add labels for axes
        plt.xlabel('Clean PFF Grade', size=6, color='green')
        plt.ylabel('Under Pressure PFF Grade', size=6, color='red')

        # Annotate with QB name and year
        for i in xy.index:
            plt.annotate(f"{xy['name'][i]}", (xy['x'][i] + .35, xy['y'][i] + .5), fontsize=5)

            plt.annotate('Great Clean and Pressured', (90, 90), fontsize=7, color='green')
            plt.annotate('Great Pressured but not Clean?', (40, 90), fontsize=7, color='purple')
            plt.annotate('Poor Clean and Pressured', (40, 30), fontsize=7, color='red')
            plt.annotate('Poor Pressured but Great Clean', (90, 30), fontsize=7, color='purple')

            # Add a title
            plt.suptitle(f' 2022 College PFF Clean Pocket Grade vs. PFF Under Pressure Grade', fontsize=15)
            plt.title(f'Min. 200 Dropbacks \nLeague Averages: Clean Pocket Avg. ({clean_avg:.2f}), Pressured Avg. ({pressure_avg:.2f})', fontsize=7, loc = 'left')

            # Style the chart
            plt.tight_layout()  # Improves layout of the plot
            plt.show()
'''

app = playerPlotter()
app.mainloop()