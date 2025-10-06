const form = document.getElementById("resumeForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        education: [{
            degree: document.getElementById("degree").value,
            institution: document.getElementById("institution").value,
            year: document.getElementById("year").value
        }],
        skills: document.getElementById("skills").value.split(","),
        training: [{
            title: document.getElementById("training_title").value,
            from: document.getElementById("training_from").value,
            to: document.getElementById("training_to").value
        }],
        projects: [{
            name: document.getElementById("project_name").value,
            description: document.getElementById("project_desc").value
        }]
    };

    try {
        const response = await fetch("/generate-resume", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Failed to generate resume");

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${data.name.replace(" ", "_")}_Resume.docx`;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);

    } catch (err) {
        alert("Error: " + err.message);
    }
});
