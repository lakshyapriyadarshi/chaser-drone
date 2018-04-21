// Auto-generated. Do not edit!

// (in-package whycon.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetNumberOfTargetsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.number = null;
      this.threshold = null;
    }
    else {
      if (initObj.hasOwnProperty('number')) {
        this.number = initObj.number
      }
      else {
        this.number = 0;
      }
      if (initObj.hasOwnProperty('threshold')) {
        this.threshold = initObj.threshold
      }
      else {
        this.threshold = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetNumberOfTargetsRequest
    // Serialize message field [number]
    bufferOffset = _serializer.int64(obj.number, buffer, bufferOffset);
    // Serialize message field [threshold]
    bufferOffset = _serializer.int64(obj.threshold, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetNumberOfTargetsRequest
    let len;
    let data = new SetNumberOfTargetsRequest(null);
    // Deserialize message field [number]
    data.number = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [threshold]
    data.threshold = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'whycon/SetNumberOfTargetsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '110202b35d9b2f547e6475584cfb396e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 number
    int64 threshold
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetNumberOfTargetsRequest(null);
    if (msg.number !== undefined) {
      resolved.number = msg.number;
    }
    else {
      resolved.number = 0
    }

    if (msg.threshold !== undefined) {
      resolved.threshold = msg.threshold;
    }
    else {
      resolved.threshold = 0
    }

    return resolved;
    }
};

class SetNumberOfTargetsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.targets = null;
    }
    else {
      if (initObj.hasOwnProperty('targets')) {
        this.targets = initObj.targets
      }
      else {
        this.targets = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetNumberOfTargetsResponse
    // Serialize message field [targets]
    bufferOffset = _serializer.int64(obj.targets, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetNumberOfTargetsResponse
    let len;
    let data = new SetNumberOfTargetsResponse(null);
    // Deserialize message field [targets]
    data.targets = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'whycon/SetNumberOfTargetsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c4b30573202f471f13445ea520b70452';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 targets
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetNumberOfTargetsResponse(null);
    if (msg.targets !== undefined) {
      resolved.targets = msg.targets;
    }
    else {
      resolved.targets = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: SetNumberOfTargetsRequest,
  Response: SetNumberOfTargetsResponse,
  md5sum() { return 'e15bc5263e6150f9a266c2eb4b4dc901'; },
  datatype() { return 'whycon/SetNumberOfTargets'; }
};
