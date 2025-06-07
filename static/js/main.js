document.getElementById("compute").addEventListener("click", () => {
  const n = document.getElementById("n").value;
  fetch(`/api/partitions?n=${n}`)
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        document.getElementById("result").textContent = data.error;
      } else {
        const lines = [
          `${data.n}의 분할 (총 ${data.count}개):`,
          ...data.partitions
        ];
        document.getElementById("result").innerHTML =
          "<pre>" + lines.join("\n") + "</pre>";
      }
    })
    .catch(err => {
      document.getElementById("result").textContent = "서버 오류 발생";
      console.error(err);
    });
});
