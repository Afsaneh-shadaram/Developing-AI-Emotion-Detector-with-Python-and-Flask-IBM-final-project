# IBM final project "Emotion Detection application":

   ## 1- Introduction
   This project is the final project for the IBM course "Developing AI Applications with Python and Flask". For more information about the course refer to this link [here](https://www.coursera.org/programs/upwardly-global-on-coursera-tjstd/learn/python-project-for-ai-application-development?specialization=ibm-generative-ai-engineering).
   In this project, the embeddable Watson AI libraries have been used to create an emotion detection application.
   Emotion detection is the concept of sentiment analysis by extracting the emotions, like joy, sadness, anger, and so on, from statements. This makes emotion detection a very            important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on.

   In this project the following tasks have been performed:

   * Task 1: Clone the project repository
   * Task 2: Create an emotion detection application using Watson NLP library
   * Task 3: Format the output of the application
   * Task 4: Package the application
   * Task 5: Run Unit tests on application
   * Task 6: Web deployment of the application using Flask
   * Task 7: Incorporate error handling
   * Task 8: Run static code analysis using Pylint

  ## 2- Creating Emotion Detector function
     
   The emotion_detector function is in emotion_detection.py file packaged in EmotionDetection folder.
   In this function the response text is converted into a dictionary using the json library functions and the required set of emotions, including anger, disgust, fear, joy,      sadness along with their scores and the dominant emotion are extarcted.


  <img width="866" height="218" alt="3b_formatted_output_test" src="https://github.com/user-attachments/assets/2584dc4e-666f-428e-a872-3a1e83099540" />
  
  ## 3- Running Unit test on the function

   The followiing unit test has been run to test the emotion_detector function.
     

  <img width="747" height="574" alt="5a_unit_testing" src="https://github.com/user-attachments/assets/7bd79e2a-165d-40fb-b820-364fa5e423b4" />


  <img width="730" height="218" alt="5b_unit_testing_result" src="https://github.com/user-attachments/assets/d11bbe2c-b09c-4c40-b2ff-d16764253bac" />


  ## 4- Web deployment of the application using Flask with error handling

   ### 4-1- The code to deploy the application on the web
   
   The code to deploy the application on the web is in server.py file. This will enable the customer to access and use the application.
   
         
   <img width="1025" height="654" alt="final code 1" src="https://github.com/user-attachments/assets/7749aded-6415-4286-a656-135a0eb0d944" />

   <img width="1028" height="438" alt="final code 2" src="https://github.com/user-attachments/assets/39a05ab7-64a3-45e9-af45-39f2ca6a41a5" />

   ### 4-2- The output of the deployed app on the localhost:5000
   
   

<img width="761" height="735" alt="Final output in Flask" src="https://github.com/user-attachments/assets/22593aee-daa9-48ad-863f-056bf9174fcd" />


   ### 4-3- The output of the deployed app with error handling when there is no input
   

     
<img width="764" height="735" alt="output with error" src="https://github.com/user-attachments/assets/ce30bf3e-ae2b-493a-9320-9fb7f53bc93c" />


     
     


     

     
     


