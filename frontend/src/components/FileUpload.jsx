import { useState } from "react";

export default function FileUpload({ onProcessed }) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    setLoading(true);
    const file = e.target.files[0];

    const form = new FormData();
    form.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/process-audio", {
      method: "POST",
      body: form,
    });

    const data = await res.json();
    onProcessed(data);
    setLoading(false);
  };

  return (
    <div>
      <input type="file" accept="audio/*" onChange={handleUpload} />
      {loading && <p>Processing audio...</p>}
    </div>
  );
}
