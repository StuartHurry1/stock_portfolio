// Initialize EmailJS with your Public API Key
emailjs.init("hebwxyz6b1w9UFoQg"); // Replace with your actual Public API Key

// Get the contact form
const contactForm = document.getElementById("contact-form");

if (contactForm) {
    contactForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        const formData = {
            from_name: document.getElementById("name").value,
            message: document.getElementById("message").value,
        };

        const serviceID = "service_7mcj7u7"; // Replace with your Service ID
        const templateID = "template_kllrytc"; // Replace with your Template ID

        emailjs.send(serviceID, templateID, formData)
            .then(function(response) {
                alert("Email sent successfully!");
                console.log("SUCCESS:", response);
            })
            .catch(function(error) {
                alert("Failed to send email. Please try again.");
                console.error("FAILED:", error);
            });
    });
} else {
    console.error("Contact form not found!");
}
