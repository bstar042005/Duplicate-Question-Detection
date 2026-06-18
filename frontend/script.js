async function checkDuplicate() {

    const q1 = document.getElementById("q1").value;
    const q2 = document.getElementById("q2").value;

    const result = document.getElementById("result");

    if(!q1 || !q2){
        result.innerHTML =
        "⚠️ Please enter both questions";
        return;
    }

    result.innerHTML = "⏳ Checking...";

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    question1:q1,
                    question2:q2
                })
            }
        );

        const data = await response.json();

        if(data.duplicate === 1){

            result.innerHTML = `
            <div style="color:green">
                Duplicate Questions
                <br><br>
                Confidence :
                ${data.confidence}%
            </div>
            `;

        }else{

            result.innerHTML = `
            <div style="color:red">
                Not Duplicate
                <br><br>
                Confidence :
                ${data.confidence}%
            </div>
            `;

        }

    }catch(error){

        result.innerHTML =
        "❌ Backend connection failed";

        console.error(error);
    }
}