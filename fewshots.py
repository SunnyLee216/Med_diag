RANK_FEW_SHOTS = """Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
The list of diseases is as follows:
['acute laryngitis', 'viral pharyngitis', 'bronchitis', 'urti', 'tuberculosis', 'stable angina', 'unstable angina', 'epiglottitis', 'influenza', 'chagas', 'possible nstemi / stemi']
RANK: 1. viral pharyngitis; 2. urti; 3. bronchitis; 4. acute laryngitis; 5. tuberculosis; 6. possible nstemi / stemi; 7. influenza; 8. epiglottitis; 9. unstable angina; 10. chagas; 11. stable angina

Here is the information of the patient:
Age: 26; Sex: M; Initial evidence: Do you constantly feel fatigued or do you have non-restful sleep? Yes; Evidence: ; Do you have a poor diet? Yes; Do you have any family members who have been diagnosed with anemia? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: tugging; Characterize your pain: a cramp; Characterize your pain: exhausting; Do you feel pain somewhere? forehead; How intense is the pain? 5; Does the pain radiate to another location? nowhere; How precisely is the pain located? 2; How fast did the pain appear? 0; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you constantly feel fatigued or do you have non-restful sleep? Yes; Do you have chronic kidney failure? Yes; Have you recently had stools that were black (like coal)? Yes; Are you taking any new oral anticoagulants ((NOACs)? Yes; Is your skin much paler than usual? Yes; Have you traveled out of the country in the last 4 weeks? N; Is your BMI less than 18.5, or are you underweight? Yes
The list of diseases is as follows:
['myocarditis', 'anaphylaxis', 'anemia', 'guillain-barré syndrome', 'cluster headache', 'acute pulmonary edema', 'sle', 'chagas', 'myasthenia gravis', 'acute dystonic reactions', ]
RANK: 1. anemia; 2. anaphylaxis; 3. myocarditis; 4. acute pulmonary edema; 5. panic attack; 6. guillain-barré syndrome; 7. chagas; 8. sle; 9. acute dystonic reactions; 10. myasthenia gravis; 11. cluster headache
"""
# Here is the information of the patient:
# Age: 64; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: sharp; Do you feel pain somewhere? ear(R); Do you feel pain somewhere? ear(L); How intense is the pain? 6; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 1; Do you have a fever (either felt or measured with a thermometer)? Yes; Are you more irritable or has your mood been very unstable recently? Yes; Do you have nasal congestion or a clear runny nose? Yes; Have you traveled out of the country in the last 4 weeks? N
# The list of diseases is as follows:
# ['chagas', 'urti', 'acute otitis media']
# RANK: 1. acute otitis media; 2. urti; 3. chagas

# Here is the information of the patient:
# Age: 6; Sex: M; Initial evidence: Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; Evidence: ; Do you have a known severe food allergy? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sharp; Do you feel pain somewhere? flank(L); Do you feel pain somewhere? iliac fossa(R); Do you feel pain somewhere? iliac fossa(L); Do you feel pain somewhere? hypochondrium(R); How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 1; How fast did the pain appear? 8; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; What color is the rash? pink; Do your lesions peel off? N; Is the rash swollen? 4; Where is the affected region located? back of the neck; Where is the affected region located? biceps(R); Where is the affected region located? biceps(L); Where is the affected region located? mouth; Where is the affected region located? thyroid cartilage; How intense is the pain caused by the rash? 1; Is the lesion (or are the lesions) larger than 1cm? Y; How severe is the itching? 8; Do you have swelling in one or more areas of your body? Yes; Where is the swelling located? nose; Have you noticed a high pitched sound when breathing in? Yes; Have you traveled out of the country in the last 4 weeks? N; Have you noticed a wheezing sound when you exhale? Yes; Are you more likely to develop common allergies than the general population? Yes
# The list of diseases is as follows:
# ['anaphylaxis', 'pulmonary embolism', 'croup', 'bronchospasm / acute asthma exacerbation', 'scombroid food poisoning', 'anemia', 'inguinal hernia', 'larygospasm', 'psvt', 'gerd', 'guillain-barré syndrome', 'atrial fibrillation', 'myocarditis', 'myasthenia gravis', 'acute dystonic reactions','sle', 'chagas']
# RANK: 1. anaphylaxis; 2. bronchospasm / acute asthma exacerbation; 3. pulmonary embolism; 4. croup; 5. scombroid food poisoning; 6. anemia; 7. inguinal hernia; 8. larygospasm; 9. psvt; 10. gerd; 11. guillain-barré syndrome; 12. atrial fibrillation; 13. myocarditis; 14. sle; 15. acute dystonic reactions; 16. myasthenia gravis; 17. chagas

CHOOSE_FWE_SHOTS = """EXAMPLE 1:
Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
The list of diseases is as follows:
['acute laryngitis', 'viral pharyngitis', 'bronchitis', 'urti', 'tuberculosis', 'stable angina', 'unstable angina', 'epiglottitis', 'influenza', 'chagas', 'possible nstemi / stemi']
ANSWER: viral pharyngitis
"""
RETHINK_FEW_SHOTS = """EXAMPLE 1:
Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
Here is the previous ranking:
1. viral pharyngitis; 2. urti; 3. bronchitis; 4. acute laryngitis; 5. tuberculosis; 6. possible nstemi / stemi; 7. influenza; 8. epiglottitis; 9. unstable angina; 10. chagas; 11. stable angina
This is the knowledge of the top 1 diseases:
Symptoms of viral pharyngitis include pain, scratchiness, difficulty swallowing, fever, fatigue, and swollen glands in the neck or jaw. The causative agent and the affected person's immune capacity can affect the severity of the symptoms. Treatment mainly aims to alleviate the symptoms, but if bacterial pharyngitis is suspected, antibiotics are needed to avoid potential complications. It is best to consult a doctor if the symptoms don't go away in a week.
You previously thought that viral pharyngitis was the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:YES
EXPLANATION:Based on the patient's symptoms, the presence of a fever, contact with a person with similar symptoms, living with multiple people, working in a daycare, pain in the tonsils, thyroid cartilage, palate, and under the jaw, along with nasal congestion and a cough, viral pharyngitis remains the most likely diagnosis. The patient's symptoms align well with the common symptoms of viral pharyngitis, including pain, fever, and swollen glands in the neck or jaw. Additionally, the patient's environment and exposure to others with similar symptoms increase the likelihood of a contagious illness such as viral pharyngitis.

EXAMPLE 2:
Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
Here is the previous ranking:
1. anemia; 2. anaphylaxis; 3. myocarditis; 4. acute pulmonary edema; 5. panic attack; 6. guillain-barré syndrome; 7. chagas; 8. sle; 9. acute dystonic reactions; 10. myasthenia gravis; 11. cluster headache
This is the knowledge of the top 1 diseases:
Symptoms of anemia include tiredness, weakness, and other complications depending on the severity of the condition. Anemia can be caused by a variety of factors, including iron deficiency, chronic diseases, pregnancy, heavy menstrual bleeding, vitamin B12 deficiency, and inadequate iron intake for infants and children. Medical treatment for anemia depends on the specific cause and may include taking supplements, undergoing medical procedures, and consuming a healthy, varied diet.
You previously thought that anemia was the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:NO
EXPLANATION:Based on the patient's symptoms, such as fever, pain in the tonsils, thyroid cartilage, palate, and under the jaw, nasal congestion, and cough, anemia is not the most likely diagnosis. The patient's symptoms do not align with the common symptoms of anemia, which include tiredness and weakness. The patient's symptoms and environment suggest a contagious illness or infection, which is not consistent with anemia. Therefore, the previous diagnosis of anemia is not valid for this patient.

EXAMPLE 3:
Here is the information of the patient:
Age: 64; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: sharp; Do you feel pain somewhere? ear(R); Do you feel pain somewhere? ear(L); How intense is the pain? 6; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 1; Do you have a fever (either felt or measured with a thermometer)? Yes; Are you more irritable or has your mood been very unstable recently? Yes; Do you have nasal congestion or a clear runny nose? Yes; Have you traveled out of the country in the last 4 weeks? N
Here is the previous ranking:
1. acute otitis media; 2. urti; 3. chagas
This is the knowledge of the top 1 diseases:

You previously thought that acute otitis media was the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:YES
EXPLANATION:Acute otitis media is a valid diagnosis based on the patient's symptoms, including fever, pain in both ears, nasal congestion, and recent antibiotic treatment for an ear infection. The patient's age (64 years old) puts them at a higher risk for complications related to infections. The presence of sharp, sensitive ear pain, along with fever and irritability, further supports the likelihood of acute otitis media. The patient's symptoms align well with the common symptoms of acute otitis media, making it the most likely diagnosis in this case.

EXAMPLE 4:
Here is the information of the patient:
Age: 6; Sex: M; Initial evidence: Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; Evidence: ; Do you have a known severe food allergy? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sharp; Do you feel pain somewhere? flank(L); Do you feel pain somewhere? iliac fossa(R); Do you feel pain somewhere? iliac fossa(L); Do you feel pain somewhere? hypochondrium(R); How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 1; How fast did the pain appear? 8; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; What color is the rash? pink; Do your lesions peel off? N; Is the rash swollen? 4; Where is the affected region located? back of the neck; Where is the affected region located? biceps(R); Where is the affected region located? biceps(L); Where is the affected region located? mouth; Where is the affected region located? thyroid cartilage; How intense is the pain caused by the rash? 1; Is the lesion (or are the lesions) larger than 1cm? Y; How severe is the itching? 8; Do you have swelling in one or more areas of your body? Yes; Where is the swelling located? nose; Have you noticed a high pitched sound when breathing in? Yes; Have you traveled out of the country in the last 4 weeks? N; Have you noticed a wheezing sound when you exhale? Yes; Are you more likely to develop common allergies than the general population? Yes
Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
1. bronchospasm / acute asthma exacerbation; 2. anaphylaxis; 3. pulmonary embolism; 4. croup; 5. scombroid food poisoning; 6. anemia; 7. inguinal hernia; 8. larygospasm; 9. psvt; 10. gerd; 11. guillain-barré syndrome; 12. atrial fibrillation; 13. myocarditis; 14. sle; 15. acute dystonic reactions; 16. myasthenia gravis; 17. chagas; This is the knowledge of the top 1 diseases:
This is the knowledge of the top 1 diseases:

You previously thought that bronchospasm / acute asthma exacerbation was the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:NO
EXPLANATION: While the patient does present with wheezing, shortness of breath, and difficulty breathing, which are symptoms commonly seen in bronchospasm/acute asthma exacerbation, the other symptoms point more towards anaphylaxis. The patient has a known severe food allergy, skin rash, swelling in the nose, and lightheadedness, which are more consistent with anaphylaxis. Additionally, the patient is more likely to develop common allergies than the general population. Given the combination of these factors, anaphylaxis seems to be a more likely diagnosis than bronchospasm/acute asthma exacerbation.
"""

RETHINK_FEW_SHOTS2 = """EXAMPLE 1:
Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
Here is the previous answer of the diagnosis:
viral pharyngitis
This is the knowledge of the viral pharyngitis:
Symptoms of viral pharyngitis include pain, scratchiness, difficulty swallowing, fever, fatigue, and swollen glands in the neck or jaw. The causative agent and the affected person's immune capacity can affect the severity of the symptoms. Treatment mainly aims to alleviate the symptoms, but if bacterial pharyngitis is suspected, antibiotics are needed to avoid potential complications. It is best to consult a doctor if the symptoms don't go away in a week.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:YES
EXPLANATION:Based on the patient's symptoms, the presence of a fever, contact with a person with similar symptoms, living with multiple people, working in a daycare, pain in the tonsils, thyroid cartilage, palate, and under the jaw, along with nasal congestion and a cough, viral pharyngitis remains the most likely diagnosis. The patient's symptoms align well with the common symptoms of viral pharyngitis, including pain, fever, and swollen glands in the neck or jaw. Additionally, the patient's environment and exposure to others with similar symptoms increase the likelihood of a contagious illness such as viral pharyngitis.

EXAMPLE 2:
Here is the information of the patient:
Age: 6; Sex: M; Initial evidence: Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; Evidence: ; Do you have a known severe food allergy? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sharp; Do you feel pain somewhere? flank(L); Do you feel pain somewhere? iliac fossa(R); Do you feel pain somewhere? iliac fossa(L); Do you feel pain somewhere? hypochondrium(R); How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 1; How fast did the pain appear? 8; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; What color is the rash? pink; Do your lesions peel off? N; Is the rash swollen? 4; Where is the affected region located? back of the neck; Where is the affected region located? biceps(R); Where is the affected region located? biceps(L); Where is the affected region located? mouth; Where is the affected region located? thyroid cartilage; How intense is the pain caused by the rash? 1; Is the lesion (or are the lesions) larger than 1cm? Y; How severe is the itching? 8; Do you have swelling in one or more areas of your body? Yes; Where is the swelling located? nose; Have you noticed a high pitched sound when breathing in? Yes; Have you traveled out of the country in the last 4 weeks? N; Have you noticed a wheezing sound when you exhale? Yes; Are you more likely to develop common allergies than the general population? Yes
Here is the previous answer of the diagnosis:
bronchospasm / acute asthma exacerbation; 
This is the knowledge of the bronchospasm / acute asthma exacerbation:

Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:NO
EXPLANATION: While the patient does present with wheezing, shortness of breath, and difficulty breathing, which are symptoms commonly seen in bronchospasm/acute asthma exacerbation, the other symptoms point more towards anaphylaxis. The patient has a known severe food allergy, skin rash, swelling in the nose, and lightheadedness, which are more consistent with anaphylaxis. Additionally, the patient is more likely to develop common allergies than the general population. Given the combination of these factors, anaphylaxis seems to be a more likely diagnosis than bronchospasm/acute asthma exacerbation.

EXAMPLE 3:
Here is the information of the patient:
Age: 64; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: sharp; Do you feel pain somewhere? ear(R); Do you feel pain somewhere? ear(L); How intense is the pain? 6; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 1; Do you have a fever (either felt or measured with a thermometer)? Yes; Are you more irritable or has your mood been very unstable recently? Yes; Do you have nasal congestion or a clear runny nose? Yes; Have you traveled out of the country in the last 4 weeks? N
Here is the previous answer of the diagnosis:
acute otitis media
This is the knowledge of acute otitis media:

Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
ANSWER:YES
EXPLANATION:Acute otitis media is a valid diagnosis based on the patient's symptoms, including fever, pain in both ears, nasal congestion, and recent antibiotic treatment for an ear infection. The patient's age (64 years old) puts them at a higher risk for complications related to infections. The presence of sharp, sensitive ear pain, along with fever and irritability, further supports the likelihood of acute otitis media. The patient's symptoms align well with the common symptoms of acute otitis media, making it the most likely diagnosis in this case.
"""

SCORE_FEW_SHOTS = """Here is the information of the patient:
Example1: /start
Patient condition: Age: 26; Sex: M; Initial evidence: Do you constantly feel fatigued or do you have non-restful sleep? Yes; Evidence: ; Do you have a poor diet? Yes; Do you have any family members who have been diagnosed with anemia? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: tugging; Characterize your pain: a cramp; Characterize your pain: exhausting; Do you feel pain somewhere? forehead; How intense is the pain? 5; Does the pain radiate to another location? nowhere; How precisely is the pain located? 2; How fast did the pain appear? 0; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you constantly feel fatigued or do you have non-restful sleep? Yes; Do you have chronic kidney failure? Yes; Have you recently had stools that were black (like coal)? Yes; Are you taking any new oral anticoagulants ((NOACs)? Yes; Is your skin much paler than usual? Yes; Have you traveled out of the country in the last 4 weeks? N; Is your BMI less than 18.5, or are you underweight? Yes.
Diagnostic result: urti.
Explanation: Based on the patient's symptoms of diffuse muscle pain, increased sweating, pain in the back of head, side of neck, and temple, along with fatigue, chills, and a rash on the forehead, it is more likely that the patient is suffering from influenza rather than urti. Cluster headache and anemia do not align with the patient's symptoms.
Scoring:
Diagnostic Coherence: Score: 2;
Severity of Symptoms: Score: 4; 
Explanation Comprehensiveness: Score: 4;
Alignment with Current Medical Knowledge: Score: 3;
TOTAL_SCORE: 13;
Example1: /end

Example2: /start
Patient condition: Age: 6; Sex: M; Initial evidence: Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; Evidence: ; Do you have a known severe food allergy? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sharp; Do you feel pain somewhere? flank(L); Do you feel pain somewhere? iliac fossa(R); Do you feel pain somewhere? iliac fossa(L); Do you feel pain somewhere? hypochondrium(R); How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 1; How fast did the pain appear? 8; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; What color is the rash? pink; Do your lesions peel off? N; Is the rash swollen? 4; Where is the affected region located? back of the neck; Where is the affected region located? biceps(R); Where is the affected region located? biceps(L); Where is the affected region located? mouth; Where is the affected region located? thyroid cartilage; How intense is the pain caused by the rash? 1; Is the lesion (or are the lesions) larger than 1cm? Y; How severe is the itching? 8; Do you have swelling in one or more areas of your body? Yes; Where is the swelling located? nose; Have you noticed a high pitched sound when breathing in? Yes; Have you traveled out of the country in the last 4 weeks? N; Have you noticed a wheezing sound when you exhale? Yes; Are you more likely to develop common allergies than the general population? Yes.
Diagnostic result: Anaphylaxis.
Explanation: The patient's symptoms, including skin rash, difficulty breathing, throat swelling, and low blood pressure, are consistent with anaphylaxis. The presence of a known severe food allergy further supports this diagnosis. Immediate medical attention is required, and epinephrine is the primary treatment for anaphylaxis.
Scoring:
Diagnostic Coherence: Score: 5; 
Severity of Symptoms: Score: 5;
Explanation Comprehensiveness: Score: 4;
Alignment with Current Medical Knowledge: Score: 5;
TOTAL_SCORE: 19;
Example2: /end 


Example3: /start
Patient condition:Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
Diagnostic result: anemia
Explanation: Based on the patient's symptoms of diffuse muscle pain, increased sweating, pain in the back of head.obiI10Jo5a .its hitia=Dd a rash on the forehead, it is more likely that the Patient is suffering from influenza rather than URTI.uster headache and anemia do not align with the patient's symptoms.
Scoring:
Diagnostic Coherence: Score: 1; 
Severity of Symptoms: Score: 3; 
Explanation Comprehensiveness: Score: 2; 
Alignment with Current Medical Knowledge: Score: 2; 
TOTAL_SCORE: 8;
Example3: /end 
"""

REFLECTIONS = """
Previous Trial:
.....
.....

Reflections:


Previous Trial:
....
....
Reflections:
"""