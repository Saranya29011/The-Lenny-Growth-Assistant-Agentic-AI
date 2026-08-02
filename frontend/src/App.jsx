import { useEffect, useState } from "react";
import API from "./services/api";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import ArtifactViewer from "./components/ArtifactViewer";


function App() {

  const [sessions, setSessions] = useState([]);
  const [currentSession, setCurrentSession] = useState("");

  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);

  const [artifact, setArtifact] = useState(null);



  useEffect(() => {
    loadSessions();
  }, []);



  useEffect(() => {

    if (currentSession) {
      loadMessages(currentSession);
    }

  }, [currentSession]);




  const loadSessions = async () => {

    try {

      const res = await API.get("/sessions");

      setSessions(res.data);


      if (
        res.data.length > 0 &&
        !currentSession
      ) {

        setCurrentSession(
          res.data[0].id
        );

      }


    } catch(err) {

      console.error(err);

    }

  };





  const loadMessages = async(sessionId)=>{

    try {

      const res =
        await API.get(
          `/messages/${sessionId}`
        );


      setMessages(res.data);


    } catch(err){

      console.error(err);

    }

  };





  const createSession = async()=>{

    try {

      await API.post("/sessions");

      await loadSessions();


    } catch(err){

      console.error(err);

    }

  };







  const sendMessage = async()=>{


    if(
      !message.trim() ||
      !currentSession
    ){
      return;
    }



    setLoading(true);



    try {


      const userMessage = message;


      setMessage("");



      const res =
        await API.post(
          "/chat",
          {
            session_id: currentSession,
            message:userMessage
          }
        );



      console.log(
        "CHAT RESPONSE:",
        res.data
      );





      if(
        res.data.artifact === true
      ){

        setArtifact(
          res.data.response
        );


        await loadMessages(
          currentSession
        );


        await loadSessions();


        return;

      }





      setArtifact(null);



      await loadMessages(
        currentSession
      );


      await loadSessions();



    } catch(err){

      console.error(err);

    }
    finally{

      setLoading(false);

    }

  };







  const deleteSession = async(sessionId)=>{


    try {


      await API.delete(
        `/sessions/${sessionId}`
      );


      await loadSessions();



      setMessages([]);

      setArtifact(null);



      if(
        currentSession === sessionId
      ){

        setCurrentSession("");

      }



    }catch(err){

      console.error(err);

    }

  };






  return (

<div
style={{
  display:"flex",
  height:"100vh",
  width:"100%",
  overflow:"hidden",
  background:"#f9fafb"
}}
>


{/* SIDEBAR */}

<Sidebar

sessions={sessions}

currentSession={currentSession}

setCurrentSession={setCurrentSession}

createSession={createSession}

deleteSession={deleteSession}

/>






{/* MAIN AREA */}

<div
style={{
 flex:1,
 display:"flex",
 overflow:"hidden"
}}
>






{/* CHAT SECTION */}

<div
style={{
 width: artifact ? "50%" : "100%",
 display:"flex",
 flexDirection:"column",
 background:"#ffffff",
 transition:"width 0.3s ease"
}}
>





{/* HEADER */}

<div
style={{
 padding:"18px 25px",
 borderBottom:"1px solid #e5e7eb"
}}
>


<h2
style={{
 margin:0,
 fontSize:"24px"
}}
>
Lenny Growth Assistant
</h2>



<p
style={{
 marginTop:"5px",
 color:"#6b7280",
 fontSize:"14px"
}}
>
Product Management & Growth Intelligence
</p>


</div>






{/* CHAT MESSAGES */}

<div
style={{
 flex:1,
 overflowY:"auto",
 padding:"25px"
}}
>


<ChatWindow
messages={messages}
/>



{
loading &&

<div
style={{
 color:"#6b7280",
 marginTop:"10px"
}}
>
Lenny is thinking...
</div>

}



</div>






{/* INPUT */}

<div
style={{
 borderTop:"1px solid #e5e7eb",
 background:"#fff"
}}
>


<MessageInput

message={message}

setMessage={setMessage}

sendMessage={sendMessage}

loading={loading}

/>


</div>




</div>









{/* ARTIFACT VIEWER */}

{
artifact &&

<div
style={{
 width:"50%",
 borderLeft:"1px solid #e5e7eb",
 background:"#ffffff",
 display:"flex",
 flexDirection:"column"
}}
>




<div
style={{
 padding:"15px",
 borderBottom:"1px solid #e5e7eb",
 fontWeight:"600",
 fontSize:"18px"
}}
>

Artifact Viewer

</div>





<div
style={{
 flex:1,
 overflow:"hidden"
}}
>


<ArtifactViewer

artifact={artifact}

/>


</div>





</div>

}




</div>


</div>

  );

}



export default App;