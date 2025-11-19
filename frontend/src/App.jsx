import { useState } from "react";
import FileUpload from "./components/FileUpload";
import StoryView from "./components/StoryView";

export default function App() {
  const [data, setData] = useState(null);

  return (
    <div className="container">
      <h1>Grandpa Story Processor</h1>
      <FileUpload onProcessed={setData} />

      {data && <StoryView story={data} />}
    </div>
  );
}
