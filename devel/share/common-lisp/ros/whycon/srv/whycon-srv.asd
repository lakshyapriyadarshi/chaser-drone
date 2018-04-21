
(cl:in-package :asdf)

(defsystem "whycon-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetNumberOfTargets" :depends-on ("_package_SetNumberOfTargets"))
    (:file "_package_SetNumberOfTargets" :depends-on ("_package"))
  ))