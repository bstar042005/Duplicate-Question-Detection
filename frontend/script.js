async function checkDuplicate() {

    const q1 =
        document.getElementById("q1").value;

    const q2 =
        document.getElementById("q2").value;

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
    document.getElementById("result").innerHTML =
        ` Duplicate Questions<br>
         Confidence: ${data.confidence}%`;
    }
    else{
    document.getElementById("result").innerHTML =
        ` Not Duplicate Questions<br>
         Confidence: ${data.confidence}%`;
    }
}