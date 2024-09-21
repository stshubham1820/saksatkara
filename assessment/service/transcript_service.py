import requests
import time
import os

class TranscriptService:
    base_url = os.environ.get('ASSEMBLYAI_URL')
    headers = {
        "authorization": os.environ.get('AUTH_KEY')
    }
    def process_utterance(self, utterances):
        resultTranscript = []
        for utterance in utterances:
            
            speaker = utterance['speaker']
            text = utterance['text']
            start_time = utterance['start']
            end_time = utterance['end']
            
            resultTranscript.append({
                
                'speaker': speaker,
                'text': text,
                'start_time': start_time,
                'end_time': end_time,
                'duration': end_time - start_time
            })

        return resultTranscript
    
    def get_transcript(self,upload_url):
        data = {
            "audio_url": upload_url,
            "speaker_labels": True,
            "entity_detection": True,
            "language_detection": False,
            "auto_chapters": True
        }

        url = self.base_url + "/transcript"
        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 200:
            response_json = response.json()
            if "id" in response_json:
                transcript_id = response_json["id"]
                polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

                while True:
                    transcription_result = requests.get(polling_endpoint, headers=self.headers).json()
                    if transcription_result['status'] == 'completed':
                        entities = transcription_result['entities']
                        utterances = transcription_result['utterances']
                        raw_text = transcription_result.get('text')
                        utterances = self.process_utterance(utterances)
                        return utterances,raw_text

                    elif transcription_result['status'] == 'error':
                        raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

                    else:
                        time.sleep(1)

            else:
                raise RuntimeError("Transcript ID not found in the response")