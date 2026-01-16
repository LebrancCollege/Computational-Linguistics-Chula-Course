# Computational Linguistics

## Week 01

### Text

- How to get the text?
  - Text File
  - PDF File
  - Internet
  - API Call
  - RSS Feed 
- Data Clean
  - Depend on what do you want to study.
- Regular Expression (RegEx)
  - Language used to Specify and Match Patterns of Characters.
- Unicode
  - String Encryption 
  - Each character has its own code.
- Metacharacters
- Grouping
  - ภาษาไทยใช้ Unicode จาก ก ถึง การันต์ ไม่ก็ถึงตัวเลขไทย 
- Quantifier
- Three regexes 
  ```py
  import re
  re.sub(<Pattern Match>, <Replace with>, ...)
  ```
- Variation of Languages (Sociolinguistic Factors)
- Complexity of Language 
  - Language has structure
    - Discourse: List of Sentences
    - Syntax: Sentence and Phrase Structure
    - Morphology: Structure of a word.
  - Linguistics Structure
    - Phonetics 
    - Phonology
    - Morphology
    - Syntax 
    - Semantics
    - Pragmatics
- Common Linguistic Analysis
  - Word Segmentation
    - Rule-Based Word Segmentation
      - Example
        - Segment "Got a long list of ex-lovers, they'll tell you I'm insane (Yeah)"
        - What are the regular expression rule for the segmentation?
      - Example
        - themendinehere 
        - Possible Segmentation (Dictionary-Based)
      - Maximal Matching Algorithm  
    - Dictionary-Based 
    - Machine Learning System
    - Token
  - Sentence Segmentation
  - Morphological Analysis
- คำเป็นหน่วยทางทฤษฎี เป็นสิ่งที่ถูกสร้างขึ้นมา 

### Word Segmentation 

### Machine Learning

- Machine Learning is very accurate. 

### Subword Tokenization

- Token => หน่วยเล็กที่สุดที่อยากได้ / ตัวอักษรที่เกิดเห็นร่วมกันมากที่สุด 
- Three Common Algorithms
  - Byte-Pair Encoding (BPE)
  - Unigram Language Modeling Tokenization 
  - WordPiece
- Byte-Pair Encoding (BPE)
  - มี Corpus กับเซตของ Vocabulary (เป็นตัวอักษร)
  - หาว่าเจอชุดตัวอักษรไหนเยอะที่สุดใน Corpus
  - ลองเอามา Merge กัน  
  - เอามาใส่ในเซตของ Vocabulary 
  - Example
      - Corpus: low low low low low lowest lowest newer newer newer newer newer newer wider
wider wider new new  

### Sentence Segmentation 

Sentence
- เหนือกว่าวลี 
- หน่วยทางไวยากรณ์ (มีภาคประธาน + ภาคแสดง) 
- Sentence Boundary Detection 

### Morphological Analysis / Normalization 

- การวิเคราะห์หน่วยคำ 
- Morphology => หน่วยคำ 

## Week 02: Machine Learning for NLP 

### Traditional Technique
- Supervised Learning  
  - Learning from Label between Input and Output. 
- Unsupervised Learning 
  - Input such an Natural Grouping 
- Transfer Learning
  - Transfer จากแหล่งที่ไม่ใช้ Input / Output ชัดเจน ไปสู่จุดที่มี Input / Output 
  - Pre-Training Process 
  - Fine-Tuning Process 

### Topic Modeling 

### Text Classification 

### Other Example
- Automatic Essay Grading 
  - ใช้ในการสอบแบบ TOEFL, IELTS ที่จะมีการตรวจแบบออนไลน์  

### Type of Classifier
- Rule-Based
  - รับ Input -> เข้ากฏ -> ส่ง Output ตามกฏ 
  - เช่น เช็คอีเมล เช็คที่อยู่ 
    - ใช้ RegEx หรือ Lexicon ก็ได้ 
- Zero-shot LLM Classifier
  - Prompt แล้วทำให้กลายเป็น Classifier ได้เลย 
  - Zero-shot => ไม่ใช้ Training Data เลย
  - เช่น GPT, Gemini, etc.  
  - ไม่ต้องเก็บข้อมูล แต่ทำได้หลายอย่าง  
- ML-Based classifier
  - Popular Model
    - Logistic Regression 
    - Deep Learning 
  Steps
    - Data Prepare
      - เตรียมข้อมูล
    - Data Annotation
      - การกำกับข้อมูล 
      - กำหนด Label / Tag 
    - Feature Engineering 
      - เอา String / คำ มาแปลงเป็นค่าตัวเลข (ที่ยังเก็บความหมาย) เพื่อนำไปวิเคราะห์ 
      - Feature Vector   
      - Example 
        - Bag-of-Word Features 
    - Model Training 
      - Train-Validation-Test
        - Training Set => เอาไว้ฝึก  _
        - Validation Set => Development Set / Holdout Set
        - Test Set => เอาไว้ทดสอบ  
      - Deduplication
        - เอาตัวที่ซ้ำในแต่ละเซตออก  
      - Inference 
        - มี Text ใหม่มาเพื่อทำการอนุมาน 
    - Evaluation  
      - พัฒนาโมเดล
      - Example
        - Spam Classification 
      - Gold Standard => คำตอบจริง
      - Prediction => คำตอบจากการคาดการณ์  
      - Precision and Recall
        - Precision: Predict A ถูกกี่ครั้ง / จำนวนครั้งที่เรา Predict A 
          - เลือกแบบจุกจิก 
        - Recall: Predict A ถูกกี่ครั้ง / จำนวนครั้งที่ A ถูก  
          - เลือกแบบกวาดเข้ามา 
        - เอามาดูกับหลายตัวเลือก แล้วดูว่ามาตรวัดมันโอเคหรือไม่ 
      - F1 Score 
        - การเฉลี่ย Precision กับ Recall 
        - 2PR / (P + R)
      - Macro-Average 
        - เอา F1 Score แต่ละตัวมาเฉลี่ยเป็นค่าค่าเดียว 
