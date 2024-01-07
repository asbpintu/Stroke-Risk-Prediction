# Stroke-Risk-Prediction


Embark on a groundbreaking journey into the future of healthcare with our innovative project - "Brain Stroke Risk Prediction".

Our project revolves around the creation of a robust predictive model designed to assess an individual's risk of experiencing a brain stroke. By harnessing the power of data science, machine learning, and comprehensive medical data, we aim to provide early warnings and personalized interventions, revolutionizing the landscape of personalized healthcare.


The project kicks off with meticulous data collection and preprocessing. Diverse datasets, comprising demographic information, medical history, lifestyle factors, and genetic markers, are curated and subjected to rigorous preprocessing techniques. This ensures data reliability, a critical aspect for the subsequent stages of our project.

### Dataset Url

[https://drive.google.com/file/d/1wzvRf9zGZi6rztGd4m8vdzhGriAmfF9j/view?usp=sharing](https://drive.google.com/file/d/1wzvRf9zGZi6rztGd4m8vdzhGriAmfF9j/view?usp=sharing)


## Steps to Run

### 1. Clone the Repository

#### [Stroke Risk Prediction](https://github.com/asbpintu/Stroke-Risk-Prediction.git)

+ [https://github.com/asbpintu/Stroke-Risk-Prediction.git](https://github.com/asbpintu/Stroke-Risk-Prediction.git)

### 2. Create Environment

#### Conda Environment

```bash
conda create --name stroke python=3.9
```
#### Python Virtual Environment

```bash
python3.9 -m venv stroke

```

### 3. Activate Environment

+ *conda activate stroke* or *activate stroke* 

+ for virtual env: - *.\stroke\Scripts\activate*
 

### 4. Install the Requirements
```bash
pip install -r requirements.txt
```



### 5. Run App

```bash
python app.py
```

Now Click [CTRl + Left_Click] on the Local or Network Url to run App

or

click here [http://localhost:8080/](http://localhost:8080/)

Now Enter Details and Predict


### 6. Train Model

Click Training to go to Training Page and Click Start Training button.


## Snapshots

![image-1](snapshots\Screenshot_15.png)
![image-2](snapshots\Screenshot_16.png)
![image-3](snapshots\Screenshot_17.png)
![image-4](snapshots\Screenshot_18.png)
![image-5](snapshots\Screenshot_19.png)
![image-6](snapshots\Screenshot_20.png)
![image-7](snapshots\Screenshot_21.png)
![image-8](snapshots\Screenshot_22.png)



## Conclusion:

In a world where technology and healthcare converge to shape the future, our "Brain Stroke Risk Prediction" project stands as a beacon of innovation. By harnessing data and machine learning, we are opening new avenues for early intervention and emphasizing the immense potential of collaboration between medical professionals and data scientists. The journey from conception to realization paves the way for a healthier future, where the specter of strokes can be proactively addressed, changing lives for the better.

# ----------------------------
# ----------------
# --------

## Deployment in AWS with Github-Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	* Policy:

        1. AmazonEC2ContainerRegistryFullAccess

        2. AmazonEC2FullAccess
    * Save the Secret Id and Key
	
### 3. Create ECR repo to store/save docker image

        - Save the URI

### 4. Create EC2 machine

        - Ubuntu os
        - CLI

### 5. Open EC2 and Install docker in EC2 Machine:
	
        sudo apt-get update -y

        sudo apt-get upgrade
        

        * curl -fsSL https://get.docker.com -o get-docker.sh

        * sudo sh get-docker.sh

        * sudo usermod -aG docker ubuntu

        * newgrp docker
	
### 6. Configure EC2 as self-hosted runner:

        * from GITHUB
            - Setting > Actions > Runner > New self hosted runner
            - Choose os Ubuntu/Linux
        * Copy the commands one by one and run in EC2 Machine

### 7. Setup github secrets:

        * from GITHUB
            - Setings > Secret and variables > Actions > Secter - Repository secret - New repository secret
            - Add all below secret one by one

        AWS_ACCESS_KEY_ID

        AWS_SECRET_ACCESS_KEY

        AWS_REGION

        AWS_ECR_LOGIN_URI

        ECR_REPOSITORY_NAME

### 8. Now after a new commit the Deplyment process start

        - Check at GITHUB Action or
        - Click the running circle button near the new commit message


# <p style="text-align: center; color: gold">THANK YOU !!!</p>

### **BestRegards**

**Ardhendu Shekhar Behera**

email - [asbpintu@gmail.com](asbpintu@gmail.com)

linkedin - [https://www.linkedin.com/in/asbpintu/](https://www.linkedin.com/in/asbpintu/)