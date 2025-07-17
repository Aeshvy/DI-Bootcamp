import React from "react";

const Exercise4 = () => {
  const handlePost = async () => {
    const url = "https://webhook.site/f43095d6-fdc8-4974-8daa-058a4a63a525";

    const payload = {
      key1: "myusername",
      email: "mymail@gmail.com",
      name: "Isaac",
      lastname: "Doe",
      age: 27,
    };

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      console.log("✅ Response from server:", data);
    } catch (error) {
      console.error("❌ Error posting data:", error);
    }
  };

  return (
    <div>
      <button onClick={handlePost}>Press me to post some data</button>
    </div>
  );
};

export default Exercise4;
