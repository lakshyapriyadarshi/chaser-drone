; Auto-generated. Do not edit!


(cl:in-package whycon-srv)


;//! \htmlinclude SetNumberOfTargets-request.msg.html

(cl:defclass <SetNumberOfTargets-request> (roslisp-msg-protocol:ros-message)
  ((number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0)
   (threshold
    :reader threshold
    :initarg :threshold
    :type cl:integer
    :initform 0))
)

(cl:defclass SetNumberOfTargets-request (<SetNumberOfTargets-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetNumberOfTargets-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetNumberOfTargets-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name whycon-srv:<SetNumberOfTargets-request> is deprecated: use whycon-srv:SetNumberOfTargets-request instead.")))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <SetNumberOfTargets-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader whycon-srv:number-val is deprecated.  Use whycon-srv:number instead.")
  (number m))

(cl:ensure-generic-function 'threshold-val :lambda-list '(m))
(cl:defmethod threshold-val ((m <SetNumberOfTargets-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader whycon-srv:threshold-val is deprecated.  Use whycon-srv:threshold instead.")
  (threshold m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetNumberOfTargets-request>) ostream)
  "Serializes a message object of type '<SetNumberOfTargets-request>"
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'threshold)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetNumberOfTargets-request>) istream)
  "Deserializes a message object of type '<SetNumberOfTargets-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'threshold) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetNumberOfTargets-request>)))
  "Returns string type for a service object of type '<SetNumberOfTargets-request>"
  "whycon/SetNumberOfTargetsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetNumberOfTargets-request)))
  "Returns string type for a service object of type 'SetNumberOfTargets-request"
  "whycon/SetNumberOfTargetsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetNumberOfTargets-request>)))
  "Returns md5sum for a message object of type '<SetNumberOfTargets-request>"
  "e15bc5263e6150f9a266c2eb4b4dc901")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetNumberOfTargets-request)))
  "Returns md5sum for a message object of type 'SetNumberOfTargets-request"
  "e15bc5263e6150f9a266c2eb4b4dc901")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetNumberOfTargets-request>)))
  "Returns full string definition for message of type '<SetNumberOfTargets-request>"
  (cl:format cl:nil "int64 number~%int64 threshold~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetNumberOfTargets-request)))
  "Returns full string definition for message of type 'SetNumberOfTargets-request"
  (cl:format cl:nil "int64 number~%int64 threshold~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetNumberOfTargets-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetNumberOfTargets-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetNumberOfTargets-request
    (cl:cons ':number (number msg))
    (cl:cons ':threshold (threshold msg))
))
;//! \htmlinclude SetNumberOfTargets-response.msg.html

(cl:defclass <SetNumberOfTargets-response> (roslisp-msg-protocol:ros-message)
  ((targets
    :reader targets
    :initarg :targets
    :type cl:integer
    :initform 0))
)

(cl:defclass SetNumberOfTargets-response (<SetNumberOfTargets-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetNumberOfTargets-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetNumberOfTargets-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name whycon-srv:<SetNumberOfTargets-response> is deprecated: use whycon-srv:SetNumberOfTargets-response instead.")))

(cl:ensure-generic-function 'targets-val :lambda-list '(m))
(cl:defmethod targets-val ((m <SetNumberOfTargets-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader whycon-srv:targets-val is deprecated.  Use whycon-srv:targets instead.")
  (targets m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetNumberOfTargets-response>) ostream)
  "Serializes a message object of type '<SetNumberOfTargets-response>"
  (cl:let* ((signed (cl:slot-value msg 'targets)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetNumberOfTargets-response>) istream)
  "Deserializes a message object of type '<SetNumberOfTargets-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'targets) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetNumberOfTargets-response>)))
  "Returns string type for a service object of type '<SetNumberOfTargets-response>"
  "whycon/SetNumberOfTargetsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetNumberOfTargets-response)))
  "Returns string type for a service object of type 'SetNumberOfTargets-response"
  "whycon/SetNumberOfTargetsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetNumberOfTargets-response>)))
  "Returns md5sum for a message object of type '<SetNumberOfTargets-response>"
  "e15bc5263e6150f9a266c2eb4b4dc901")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetNumberOfTargets-response)))
  "Returns md5sum for a message object of type 'SetNumberOfTargets-response"
  "e15bc5263e6150f9a266c2eb4b4dc901")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetNumberOfTargets-response>)))
  "Returns full string definition for message of type '<SetNumberOfTargets-response>"
  (cl:format cl:nil "int64 targets~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetNumberOfTargets-response)))
  "Returns full string definition for message of type 'SetNumberOfTargets-response"
  (cl:format cl:nil "int64 targets~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetNumberOfTargets-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetNumberOfTargets-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetNumberOfTargets-response
    (cl:cons ':targets (targets msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetNumberOfTargets)))
  'SetNumberOfTargets-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetNumberOfTargets)))
  'SetNumberOfTargets-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetNumberOfTargets)))
  "Returns string type for a service object of type '<SetNumberOfTargets>"
  "whycon/SetNumberOfTargets")