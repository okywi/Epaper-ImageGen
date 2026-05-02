echo "Building docker image..."
docker build -t epaper-imagegen .
echo 'Running image with env file and port...'
docker run --rm --name epaper-imagegen-container -p 72:72 epaper-imagegen
