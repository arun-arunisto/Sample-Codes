# Sample-Codes
Functions that i used for my projects
1. Number letter separator from a string

            if the word/string like this 
                  "127a301d101"
            and i want results like
                  "127,a,301,d,101"
                  or
                  "127:a:301:d:101"
                  or
                  "127-a-301-d-101"
            
            like this cases we are going to use this function
            
above code i use "," so you need to change the sign for your code!!!

            change the code where
                        "result = ",".join(result)"
                        to
                        "result = ":".join(result)"



2. List and None conversion of data that fetching from pgsql
            in one of my project i use pgsql as my db and i fetch data from it it returned data as tuple and it returned null data's as None.
                        
            ![Screenshot (47)](https://user-images.githubusercontent.com/86800553/196351363-4a8a1ef8-e1b4-40ce-939e-ecce75778eaf.png)

            like the above picture, so decide to write code to change it but unfortunately tuple doesn't support assigning values so i convert it to list then i assign the option that i want 
            after creating the function it workks fine! like this
            
            ![Screenshot (48)](https://user-images.githubusercontent.com/86800553/196351903-0fe2bb15-eebb-42c5-9f6a-cf5d39d5e79b.png)
            
            how to use the function is
            
            db_cursor.execute(
                        "select * from sampleTable"
              )
            table = db_cursor.fetchall()
            list_none_conversion(table=table) ---> my function to change the data structure and none 
           
3. Edube LED Display
            Edube part 2 string methods task to print led 7 format display code refer from stackoverflow
            
