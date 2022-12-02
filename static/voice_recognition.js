


// JSONデータ取得のWeb APIにJavaScriptからリクエストを投げ、レスポンスに応じてHTML要素を操作するサンプル
document.getElementById("get_click").addEventListener("click", (e) => {
    // ボタンイベントのキャンセル
    e.preventDefault();

    let params = new URLSearchParams();
    let gs = document.getElementById("get_click").value;
    gs = (gs && gs === "no") ? "yes" : "no";
    params.set("gs", gs);
    //console.log("log");
    //console.log(state);

    fetch("voice_recognition?" + params.toString()).then(response => {
        console.log(response.status);  // => 200

        response.json().then(data => {
            // JSONをJSオブジェクトにパースされたオブジェクトがdataに格納される
            console.log(data);  // => {...}
        });
    });
});


// JSONデータ取得のWeb APIにJavaScriptからリクエストを投げ、レスポンスに応じてHTML要素を操作するサンプル
document.getElementById("post_click").addEventListener("click", (e) => {
    // ボタンイベントのキャンセル
    e.preventDefault();

    let ps = document.getElementById("post_click").value;
    ps = (ps && ps === "no") ? "yes" : "no";

    let data = new FormData();
    data.append("ps", ps);
    //data.forEach(e => console.log("e: " + e));
    fetch("/voice_recognition?", { method: 'POST', body: data, }).then(response => {
        console.log(response.status);  // => 200

        response.json().then(data => {
            // JSONをJSオブジェクトにパースされたオブジェクトがdataに格納される
            console.log(data);  // => {...}
        });
    });
});