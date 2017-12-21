
t= ["[2017/12/21 13:37:34.926] CAFL ttesrvr.cpp                 5349 0f4c New Call object with UCID: 9261513856254552 created upon receiving an event with CID: 297643",
"[2017/12/21 13:37:34.926] CAFL TteSCstaEventHandler.cpp    1120 0f4c Delivered Event, UCID<9261513856254552> RqC<-1> , CTK:0, SubjectDID:101(R), AlertingCID:297643, AlertingDID:101(R), CallingDID:0271807(S), CalledDID:1(S), LRDID:444(S), ConsHeldDID:(N/A), CallingPartyIsANI:True, ACDDN:445, Trunk:239, TrunkGroup:-1, LCS:Alerting, Cause:CallForwardNoAnswer",
"[2017/12/21 13:37:34.926] CAFL ttetcall.cpp                 378 0f4c HandlingType and ContactType transition, UCID: 9261513856254552, New HandlingType: ProCenterExternal, New ContactType: Routed Voice.",
"[2017/12/21 13:37:34.926] CAFL TteSCstaEventHandler.cpp    1228 0f4c Queued Event, UCID<9261513856254552>, SubjectDID:101(R), QueuedCID:297643, QueuedDID:101(R), QueuedToDID:100(A), CallingDID:0271807(S), CalledDID:1(S), LRDID:(N/A), LCS:Queued, Cause:NoAvailableAgents, CallsInQueue:-1, Trunk:",
"[2017/12/21 13:37:34.926] CAFL ttescall.cpp               11129 14d0 Divert from Queue Call Request, UCID<9261513856254552>, DivertDestination: 573, Reason: DIVERT_IVR_DISTRIBUTION",
"[2017/12/21 13:37:34.989] CAFL TteSCstaEventHandler.cpp    1149 0f4c Diverted Event, UCID<9261513856254552> RqC<0> , CTK:0, SubjectDID:101(R), DivertingCID:297643, DivertingDID:101(R), DestinationDID:573(S), LCS:Null, Cause:Distributed",
"[2017/12/21 13:37:34.989] CAFL TteSCstaEventHandler.cpp    1120 0f4c Delivered Event, UCID<9261513856254552> RqC<0> , CTK:0, SubjectDID:573(S), AlertingCID:297643, AlertingDID:573(S), CallingDID:0271807(S), CalledDID:1(S), LRDID:(N/A), ConsHeldDID:(N/A), CallingPartyIsANI:True, ACDDN:N/A, Trunk:239, TrunkGroup:-1, LCS:Alerting, Cause:Distributed",
"[2017/12/21 13:37:36.785] CAFL TteSCstaEventHandler.cpp    1159 0f4c Established Event, UCID<9261513856254552> RqC<0> , SubjectDID:573(S), JoinedCID:297643, JoinedDID:573(S), AnswerDID:573(S), CallingDID:0271807(S), CalledDID:1(S), LRDID:(N/A), Trunk:239, LCS:Connected, Cause:Normal",
"[2017/12/21 13:37:46.176] CAFL ttescall.cpp                6061 14d0 One Step Transfer (Smart Transfer) Call Request, UCID<9261513856254552>, TransferringDID: 573. TransferTarget: 445",
"[2017/12/21 13:37:46.239] CAFL TteSCstaEventHandler.cpp    1260 0f4c Transferred Event, UCID<9261513856254552> RqC<0> , SubjectDID:573(S), PrimaryCID:297643, PrimaryDID:573(S), SecondaryCID:, SecondaryDID:(N/A), TransferringDID:573(S), TransferToDID:101(R), LCS:Null, Cause:SingleStepTransfer, PrivateCause:SingleStepTransfer, Parties:2[{239(N/A)}{101(R)}], NewCID:297643",
"[2017/12/21 13:37:46.239] CAFL TteSCstaEventHandler.cpp    1120 0f4c Delivered Event, UCID<9261513856254552> RqC<0> , CTK:0, SubjectDID:101(R), AlertingCID:297643, AlertingDID:101(R), CallingDID:0271807(S), CalledDID:445(S), LRDID:(N/A), ConsHeldDID:(N/A), CallingPartyIsANI:True, ACDDN:445, Trunk:239, TrunkGroup:-1, LCS:Alerting, Cause:SingleStepTransfer",
"[2017/12/21 13:37:46.239] CAFL TteSCstaEventHandler.cpp    1228 0f4c Queued Event, UCID<9261513856254552>, SubjectDID:101(R), QueuedCID:297643, QueuedDID:101(R), QueuedToDID:100(A), CallingDID:0271807(S), CalledDID:445(S), LRDID:(N/A), LCS:Queued, Cause:NoAvailableAgents, CallsInQueue:-1, Trunk:",
"[2017/12/21 13:37:46.239] CAFL TteSRoutingEventHandler.     365 10f8 EnqueueCall Event, UCID<9261513856254552>, RqC<0>, CallTypeName:INFO_GEN_LU",
"[2017/12/21 13:37:46.239] CAFL TteSRoutingEventHandler.      31 10f8 UpdateRoutingData Event, UCID<9261513856254552>, RqC<0>, OriginalDNIS:445, OriginalANI:0271807, BU key:1, CallTypeName:INFO_GEN_LU, Priority:1, CallTypeStep:0, External:0, Transfer:1",
"[2017/12/21 13:37:46.239] CAFL TteSRoutingEventHandler.      31 10f8 UpdateRoutingData Event, UCID<9261513856254552>, RqC<0>, OriginalDNIS:445, OriginalANI:0271807, BU key:1, CallTypeName:INFO_GEN_LU, Priority:1, CallTypeStep:1, External:0, Transfer:1",
"[2017/12/21 13:37:47.239] CAFL TteSRoutingEventHandler.      31 10f8 UpdateRoutingData Event, UCID<9261513856254552>, RqC<0>, OriginalDNIS:445, OriginalANI:0271807, BU key:1, CallTypeName:INFO_GEN_LU, Priority:1, CallTypeStep:2, External:0, Transfer:1",
"[2017/12/21 13:38:13.317] CAFL TteSRoutingEventHandler.      31 10f8 UpdateRoutingData Event, UCID<9261513856254552>, RqC<0>, OriginalDNIS:445, OriginalANI:0271807, BU key:1, CallTypeName:INFO_GEN_LU, Priority:1, CallTypeStep:2, External:0, Transfer:1",
"[2017/12/21 13:38:13.317] CAFL TteSRoutingEventHandler.     233 10f8 AssignCall Event, UCID<9261513856254552>, RqC<0>, UserId:101",
"[2017/12/21 13:38:13.317] CAFL ttesagnt.cpp                2089 10f8 SActiveAgent::HandleAssignCall Event. UserKey<4> UserId<101> Ext{509} HandleAssignCall Event: UCID{9261513856254552} RqC{0}",
"[2017/12/21 13:38:13.317] CAFL ttescall.cpp                7400 14d0 Divert Call Request, UCID<9261513856254552>, CID:, DivertingDID:, DivertDestination:509, CallTypeName:{INFO_GEN_LU}, CallTypeStep:2, reason:DIVERT_ROUTING",
"[2017/12/21 13:38:13.395] CAFL TteSCstaEventHandler.cpp    1149 0f4c Diverted Event, UCID<9261513856254552> RqC<0> , CTK:12, SubjectDID:101(R), DivertingCID:297643, DivertingDID:101(R), DestinationDID:509(S), LCS:Null, Cause:Distributed",
"[2017/12/21 13:38:13.395] CAFL TteSCstaEventHandler.cpp    1120 0f4c Delivered Event, UCID<9261513856254552> RqC<0> , CTK:12, SubjectDID:509(S), AlertingCID:297643, AlertingDID:509(S), CallingDID:0271807(S), CalledDID:445(S), LRDID:(N/A), ConsHeldDID:(N/A), CallingPartyIsANI:True, ACDDN:445, Trunk:239, TrunkGroup:-1, LCS:Alerting, Cause:Distributed",
"[2017/12/21 13:38:15.739] CAFL TteSCstaEventHandler.cpp    1159 0f4c Established Event, UCID<9261513856254552> RqC<0> , SubjectDID:509(S), JoinedCID:297643, JoinedDID:509(S), AnswerDID:509(S), CallingDID:0271807(S), CalledDID:445(S), LRDID:(N/A), Trunk:239, LCS:Connected, Cause:Normal",
"[2017/12/21 13:38:15.739] CAFL TteSRoutingEventHandler.     277 10f8 DequeueCall Event, UCID<9261513856254552>, RqC<0>, CallTypeName:INFO_GEN_LU",
"[2017/12/21 13:40:56.208] CAFL TteSCstaEventHandler.cpp    1140 0f4c Connection Cleared Event, UCID<9261513856254552> RqC<0> , SubjectDID:509(S), ClearedCID:297643, ClearedDID:509(S), LCS:Null, Cause:Normal Clearing",
"[2017/12/21 13:40:56.208] CAFL ttesrvr.cpp                 5933 0f4c Remove UCID<9261513856254552> from call table. Entries left:5. #CIDXRef:5. #DIDXRef:3"]


p=["[2017/12/19 09:02:52.815] CAFL TpsSUserPresence.h           444 1b70 TpsSUserPresence::UpdateStateByMediaStateEvent. Rcvd Media State Event:  UserKey{3},UserId{100},Telepony User Status Ex:{MediaStateBase:{Media{Voice},State{Logon},Cause{None}}} Acd State{ACDUNAVAIL} Extension{530} InitialAcdStateSource{ACDSTATESOURCE_CTIQUERY} SilentMonitoringInfoColl{CSM Coll:{ListDetails: {}}}},ListDetails: {[HandlingState:{ContactId/RqC{6901513666971562/-1},ContactType{None},Ca",
"[2017/12/21 13:46:14.427] CAFL TpsSUserPresence.cpp        1351 1b70 TpsSUserPresence::OnEvent. Rcvd Agent ACDAVAIL Event for UserId{110}.", 
"[2017/12/18 17:05:04.163] CAFL TpsSUserPresence.h           521 1b70 TpsSUserPresence::UpdateStateByHandlingStateEvent. Rcvd Handling State Update Event:  ANI: 022792723UserKey{8},UserId{104},ListDetails: {[HandlingState:{ContactId/RqC{4911513609482562/0},ContactType{Routed Voice},Cause{None},QueueKey{12},Priority{1},StartTime{2017/12/18 16:05:04.163},State{Talking}}]}" 
]
 
from project.log_parser.presence_log import PresenceLog
from project.log_parser.telephony_log import TelephonyLog

for s in p:
    e = PresenceLog(s)
    print (e.getUserId())
    print (e.getDate())
    print (e.getExtension())
    print (e.getAcdState())
    print (e.getLineState())
    print (e.getUcid())



        
        
for s in t:
    e = TelephonyLog(s)
    #DATA
    print (e.getDate())    
    print (e.getUcid())
    print (e.getCalling())
    print (e.getDestination())
    print (e.getNewCallUcid())
    print (e.getCallType())

for s in p:
    e=PresenceLog(s)    
    e.parse()
    
for s in t:
    e=TelephonyLog(s)    
    e.parse()