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

Here is the information of the patient:
Age: 64; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: sharp; Do you feel pain somewhere? ear(R); Do you feel pain somewhere? ear(L); How intense is the pain? 6; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 1; Do you have a fever (either felt or measured with a thermometer)? Yes; Are you more irritable or has your mood been very unstable recently? Yes; Do you have nasal congestion or a clear runny nose? Yes; Have you traveled out of the country in the last 4 weeks? N
The list of diseases is as follows:
['chagas', 'urti', 'acute otitis media']
RANK: 1. acute otitis media; 2. urti; 3. chagas
"""

RETHINK_FEW_SHOTS = """Here is the information of the patient:
Age: 19; Sex: M; Initial evidence: Do you have a fever (either felt or measured with a thermometer)? Yes; Evidence: ; Have you been in contact with a person with similar symptoms in the past 2 weeks? Yes; Do you live with 4 or more people? Yes; Do you attend or work in a daycare? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sensitive; Characterize your pain: burning; Do you feel pain somewhere? tonsil(R); Do you feel pain somewhere? tonsil(L); Do you feel pain somewhere? thyroid cartilage; Do you feel pain somewhere? palace; Do you feel pain somewhere? under the jaw; How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 10; How fast did the pain appear? 4; Do you have a fever (either felt or measured with a thermometer)? Yes; Do you have nasal congestion or a clear runny nose? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N
Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on. 
The list of diseases is as follows:
Here is the previous ranking:
['viral pharyngitis', 'urti', 'bronchitis', 'acute laryngitis', 'tuberculosis', 'possible nstemi / stemi', 'influenza', 'epiglottitis', 'unstable angina', 'chagas', 'stable angina']
Now,Here is the knwoledge serach from outside:

Regardless of whether external information exists, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid.You can change your answer at any point.\nYou should ANSWER:YES/NO and your EXPLANATION for the ANSWER you output.
"""

SCORE_FEW_SHOTS = """Here is the information of the patient:
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