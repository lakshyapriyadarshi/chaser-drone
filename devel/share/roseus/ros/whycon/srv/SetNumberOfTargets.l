;; Auto-generated. Do not edit!


(when (boundp 'whycon::SetNumberOfTargets)
  (if (not (find-package "WHYCON"))
    (make-package "WHYCON"))
  (shadow 'SetNumberOfTargets (find-package "WHYCON")))
(unless (find-package "WHYCON::SETNUMBEROFTARGETS")
  (make-package "WHYCON::SETNUMBEROFTARGETS"))
(unless (find-package "WHYCON::SETNUMBEROFTARGETSREQUEST")
  (make-package "WHYCON::SETNUMBEROFTARGETSREQUEST"))
(unless (find-package "WHYCON::SETNUMBEROFTARGETSRESPONSE")
  (make-package "WHYCON::SETNUMBEROFTARGETSRESPONSE"))

(in-package "ROS")





(defclass whycon::SetNumberOfTargetsRequest
  :super ros::object
  :slots (_number _threshold ))

(defmethod whycon::SetNumberOfTargetsRequest
  (:init
   (&key
    ((:number __number) 0)
    ((:threshold __threshold) 0)
    )
   (send-super :init)
   (setq _number (round __number))
   (setq _threshold (round __threshold))
   self)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:threshold
   (&optional __threshold)
   (if __threshold (setq _threshold __threshold)) _threshold)
  (:serialization-length
   ()
   (+
    ;; int64 _number
    8
    ;; int64 _threshold
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _number
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _number (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _number) (= (length (_number . bv)) 2)) ;; bignum
              (write-long (ash (elt (_number . bv) 0) 0) s)
              (write-long (ash (elt (_number . bv) 1) -1) s))
             ((and (class _number) (= (length (_number . bv)) 1)) ;; big1
              (write-long (elt (_number . bv) 0) s)
              (write-long (if (>= _number 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _number s)(write-long (if (>= _number 0) 0 #xffffffff) s)))
     ;; int64 _threshold
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _threshold (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _threshold) (= (length (_threshold . bv)) 2)) ;; bignum
              (write-long (ash (elt (_threshold . bv) 0) 0) s)
              (write-long (ash (elt (_threshold . bv) 1) -1) s))
             ((and (class _threshold) (= (length (_threshold . bv)) 1)) ;; big1
              (write-long (elt (_threshold . bv) 0) s)
              (write-long (if (>= _threshold 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _threshold s)(write-long (if (>= _threshold 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _number
#+(or :alpha :irix6 :x86_64)
      (setf _number (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _number (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _threshold
#+(or :alpha :irix6 :x86_64)
      (setf _threshold (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _threshold (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass whycon::SetNumberOfTargetsResponse
  :super ros::object
  :slots (_targets ))

(defmethod whycon::SetNumberOfTargetsResponse
  (:init
   (&key
    ((:targets __targets) 0)
    )
   (send-super :init)
   (setq _targets (round __targets))
   self)
  (:targets
   (&optional __targets)
   (if __targets (setq _targets __targets)) _targets)
  (:serialization-length
   ()
   (+
    ;; int64 _targets
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _targets
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _targets (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _targets) (= (length (_targets . bv)) 2)) ;; bignum
              (write-long (ash (elt (_targets . bv) 0) 0) s)
              (write-long (ash (elt (_targets . bv) 1) -1) s))
             ((and (class _targets) (= (length (_targets . bv)) 1)) ;; big1
              (write-long (elt (_targets . bv) 0) s)
              (write-long (if (>= _targets 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _targets s)(write-long (if (>= _targets 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _targets
#+(or :alpha :irix6 :x86_64)
      (setf _targets (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _targets (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass whycon::SetNumberOfTargets
  :super ros::object
  :slots ())

(setf (get whycon::SetNumberOfTargets :md5sum-) "e15bc5263e6150f9a266c2eb4b4dc901")
(setf (get whycon::SetNumberOfTargets :datatype-) "whycon/SetNumberOfTargets")
(setf (get whycon::SetNumberOfTargets :request) whycon::SetNumberOfTargetsRequest)
(setf (get whycon::SetNumberOfTargets :response) whycon::SetNumberOfTargetsResponse)

(defmethod whycon::SetNumberOfTargetsRequest
  (:response () (instance whycon::SetNumberOfTargetsResponse :init)))

(setf (get whycon::SetNumberOfTargetsRequest :md5sum-) "e15bc5263e6150f9a266c2eb4b4dc901")
(setf (get whycon::SetNumberOfTargetsRequest :datatype-) "whycon/SetNumberOfTargetsRequest")
(setf (get whycon::SetNumberOfTargetsRequest :definition-)
      "int64 number
int64 threshold
---
int64 targets

")

(setf (get whycon::SetNumberOfTargetsResponse :md5sum-) "e15bc5263e6150f9a266c2eb4b4dc901")
(setf (get whycon::SetNumberOfTargetsResponse :datatype-) "whycon/SetNumberOfTargetsResponse")
(setf (get whycon::SetNumberOfTargetsResponse :definition-)
      "int64 number
int64 threshold
---
int64 targets

")



(provide :whycon/SetNumberOfTargets "e15bc5263e6150f9a266c2eb4b4dc901")


