<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Flask Image Editor</title>
</head>
<body>
    <div class="container">
        <h1>Flask Image Editor</h1>
        <p>This Flask application allows users to upload and edit images. It supports converting images to PNG, JPG, and WebP formats, as well as converting images to grayscale.</p>

  <h2>Features</h2>
        <ul>
            <li>Upload images in various formats (PNG, JPG, JPEG, GIF, WebP)</li>
            <li>Convert images to:
                <ul>
                    <li>PNG</li>
                    <li>JPG</li>
                    <li>WebP</li>
                    <li>Grayscale</li>
                </ul>
            </li>
            <li>Download the processed images</li>
        </ul>

  <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Flask</li>
            <li>OpenCV (cv2)</li>
            <li>Werkzeug</li>
        </ul>

  <h2>Installation</h2>
        <ol>
            <li><strong>Install the required packages:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Ensure the `uploads` and `static` directories exist:</strong>
                <pre><code>mkdir uploads static</code></pre>
            </li>
        </ol>

  <h2>Usage</h2>
        <ol>
            <li><strong>Run the Flask application:</strong>
                <pre><code>python app.py</code></pre>
            </li>
            <li><strong>Open your browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</strong></li>
            <li><strong>Upload an image and select the desired operation.</strong></li>
            <li><strong>Click "Submit" to process the image.</strong></li>
            <li><strong>Download the processed image from the link provided.</strong></li>
        </ol>
    </div>
</body>
</html>
