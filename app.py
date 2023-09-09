from fastapi import FastAPI
import uvicorn
import joblib,os

app= FastAPI()

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

@app.get('/predict/{feature}')
async def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return (features, result)



@app.get("/")
def greet():
    return {"hello world"}

if __name__=="__main__":
    uvicorn.run(app)

