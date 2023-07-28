const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const section1 = document.getElementById("step1");
const section2 = document.getElementById("step2");
const section3 = document.getElementById("step3");
const gptBtn = document.getElementById("gpt-start");
const levBtn = document.getElementById("lev-start");
const downloadBtn = document.getElementById("download");
var outputCSV;
var stage = 1;

uploadButton.addEventListener("click", () => {
  if (stage > 1) return;
  fileInput.click(); // Trigger the file input click event
});

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0]; // Get the selected file
  console.log(file); // Do something with the file (e.g., upload it)
  document.getElementById(
    "selectedFileLabel"
  ).innerText = `Selected: "${file.name}"`;

  section2.style.display = "flex";
  section2.classList.add("step-show");
  stage++;
});

gptBtn.addEventListener("click", () => {
  // upload file to backend, start converting
  if (stage > 2) return;
  const files = fileInput.files; // Get the selected file
  const data = new FormData();
  for (let i = 0; i < files.length; i++) {
    data.append(`file`, files[i]);
  }
  const retVal = fetch("/uploadGPT", {
    method: "POST",
    body: data,
  })
    .then((data) => data.blob())
    .then((blob) => {
      section3.style.display = "flex";
      section3.classList.add("step-show");
      stage++;

      outputCSV = blob;
    });
});

levBtn.addEventListener("click", () => {
  // upload file to backend, start converting
  if (stage > 2) return;
  const files = fileInput.files; // Get the selected file
  const data = new FormData();
  for (let i = 0; i < files.length; i++) {
    data.append(`file`, files[i]);
  }
  const retVal = fetch("/uploadLev", {
    method: "POST",
    body: data,
  })
    .then((data) => data.blob())
    .then((blob) => {
      section3.style.display = "flex";
      section3.classList.add("step-show");
      stage++;

      outputCSV = blob;
    });
});

downloadBtn.addEventListener("click", () => {
  // download file here
  let blobUrl = URL.createObjectURL(outputCSV);
  window.location.replace(blobUrl);
  URL.revokeObjectURL(blobUrl);
});
