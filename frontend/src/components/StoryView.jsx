export default function StoryView({ story }) {
  return (
    <div className="story-box">
      <h2>Transcription</h2>
      <p>{story.transcript}</p>

      <h2>Summary</h2>
      <p>{story.summary}</p>

      <h2>Important Moments</h2>
      <ul>
        {story.highlights.map((h, i) => (
          <li key={i}>{h}</li>
        ))}
      </ul>

      <h2>Generated Story Visual</h2>
      <img
        src={`http://127.0.0.1:8000/${story.visual_image_path}`}
        style={{ width: "100%", maxWidth: "600px" }}
      />
    </div>
  );
}
