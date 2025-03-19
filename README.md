# Passiogo-extension
Bus-Tracker 🚍📲
An Extension of the PassioGo App Using Its API

## **Why I Built This**
Tired of standing at the bus stop in freezing temperatures for no reason.

There were mornings when I had to wait up to 13 minutes in below 30°F weather, just standing there, hoping the bus would arrive soon. The worst part? The bus schedule wasn't always reliable. Sometimes the bus came early, sometimes late, and sometimes I’d check the PassioGo app over and over again, trying to guess when I should leave home.

I found myself constantly refreshing the app, opening my phone every few minutes just to check the bus location. It became a distraction and an unnecessary hassle.

So, I built Bus-Tracker, an automated solution that notifies me when the bus reaches a specific location. Now, instead of shivering at the stop, I only leave when I know my bus is about to arrive.

## **How It Works**  
 **Tracks a specific bus on my chosen route** using the **PassioGo API**.  
 **Notifies me via a Twilio phone call & text message** when the bus reaches a specific **geographical location** near my stop.  
 **Runs on AWS Lambda**, so I never have to start it manually.  
 **Saves me from standing in freezing temperatures**, while ensuring I **never miss my bus**.  

---

## **Technology Stack** 🛠  
- **PassioGo API** – Fetches real-time bus location data.  
- **Twilio API** – Sends automated phone calls and SMS alerts.  
- **AWS Lambda** – Runs the function at scheduled times.  
- **Python** – Core implementation.  

---

## **Setup & Deployment** 

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/bus-tracker.git
cd bus-tracker
```

## **Future Plans **
Right now, this works perfectly for me—I no longer freeze at the stop or constantly check my phone.

But in the future, I want to expand it so anyone can:
 Track any bus on any route
 Get alerts for any stop or custom GPS location
 Have a simple UI to configure their own bus tracking
