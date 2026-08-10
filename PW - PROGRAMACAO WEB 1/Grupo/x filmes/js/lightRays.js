(function () {
  'use strict';

  var config = {
    raysOrigin: 'top-center',
    raysColor: '#FFFFFF',
    raysSpeed: 1.5,
    lightSpread: 0.8,
    rayLength: 1.2,
    pulsating: false,
    fadeDistance: 1.0,
    saturation: 1.0,
    followMouse: true,
    mouseInfluence: 0.1,
    noiseAmount: 0.1,
    distortion: 0.05
  };

  var OUTSIDE = 0.2;

  function hexToRgb(hex) {
    var m = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return m
      ? [parseInt(m[1], 16) / 255, parseInt(m[2], 16) / 255, parseInt(m[3], 16) / 255]
      : [1, 1, 1];
  }

  function getAnchorAndDir(origin, w, h) {
    switch (origin) {
      case 'top-left':
        return { anchor: [0, -OUTSIDE * h], dir: [0, 1] };
      case 'top-right':
        return { anchor: [w, -OUTSIDE * h], dir: [0, 1] };
      case 'left':
        return { anchor: [-OUTSIDE * w, 0.5 * h], dir: [1, 0] };
      case 'right':
        return { anchor: [(1 + OUTSIDE) * w, 0.5 * h], dir: [-1, 0] };
      case 'bottom-left':
        return { anchor: [0, (1 + OUTSIDE) * h], dir: [0, -1] };
      case 'bottom-center':
        return { anchor: [0.5 * w, (1 + OUTSIDE) * h], dir: [0, -1] };
      case 'bottom-right':
        return { anchor: [w, (1 + OUTSIDE) * h], dir: [0, -1] };
      default:
        return { anchor: [0.5 * w, -OUTSIDE * h], dir: [0, 1] };
    }
  }

  var vertexShader = [
    'attribute vec2 position;',
    'varying vec2 vUv;',
    'void main() {',
    '  vUv = position * 0.5 + 0.5;',
    '  gl_Position = vec4(position, 0.0, 1.0);',
    '}'
  ].join('\n');

  var fragmentShader = [
    'precision highp float;',
    '',
    'uniform float iTime;',
    'uniform vec2  iResolution;',
    '',
    'uniform vec2  rayPos;',
    'uniform vec2  rayDir;',
    'uniform vec3  raysColor;',
    'uniform float raysSpeed;',
    'uniform float lightSpread;',
    'uniform float rayLength;',
    'uniform float pulsating;',
    'uniform float fadeDistance;',
    'uniform float saturation;',
    'uniform vec2  mousePos;',
    'uniform float mouseInfluence;',
    'uniform float noiseAmount;',
    'uniform float distortion;',
    '',
    'varying vec2 vUv;',
    '',
    'float noise(vec2 st) {',
    '  return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);',
    '}',
    '',
    'float rayStrength(vec2 raySource, vec2 rayRefDirection, vec2 coord,',
    '                  float seedA, float seedB, float speed) {',
    '  vec2 sourceToCoord = coord - raySource;',
    '  vec2 dirNorm = normalize(sourceToCoord);',
    '  float cosAngle = dot(dirNorm, rayRefDirection);',
    '',
    '  float distortedAngle = cosAngle + distortion * sin(iTime * 2.0 + length(sourceToCoord) * 0.01) * 0.2;',
    '',
    '  float spreadFactor = pow(max(distortedAngle, 0.0), 1.0 / max(lightSpread, 0.001));',
    '',
    '  float distance = length(sourceToCoord);',
    '  float maxDistance = iResolution.x * rayLength;',
    '  float lengthFalloff = clamp((maxDistance - distance) / maxDistance, 0.0, 1.0);',
    '',
    '  float fadeFalloff = clamp((iResolution.x * fadeDistance - distance) / (iResolution.x * fadeDistance), 0.5, 1.0);',
    '  float pulse = pulsating > 0.5 ? (0.8 + 0.2 * sin(iTime * speed * 3.0)) : 1.0;',
    '',
    '  float baseStrength = clamp(',
    '    (0.45 + 0.15 * sin(distortedAngle * seedA + iTime * speed)) +',
    '    (0.3 + 0.2 * cos(-distortedAngle * seedB + iTime * speed)),',
    '    0.0, 1.0',
    '  );',
    '',
    '  return baseStrength * lengthFalloff * fadeFalloff * spreadFactor * pulse;',
    '}',
    '',
    'void mainImage(out vec4 fragColor, in vec2 fragCoord) {',
    '  vec2 coord = vec2(fragCoord.x, iResolution.y - fragCoord.y);',
    '',
    '  vec2 finalRayDir = rayDir;',
    '  if (mouseInfluence > 0.0) {',
    '    vec2 mouseScreenPos = mousePos * iResolution.xy;',
    '    vec2 mouseDirection = normalize(mouseScreenPos - rayPos);',
    '    finalRayDir = normalize(mix(rayDir, mouseDirection, mouseInfluence));',
    '  }',
    '',
    '  vec4 rays1 = vec4(1.0) *',
    '               rayStrength(rayPos, finalRayDir, coord, 36.2214, 21.11349,',
    '                           1.5 * raysSpeed);',
    '  vec4 rays2 = vec4(1.0) *',
    '               rayStrength(rayPos, finalRayDir, coord, 22.3991, 18.0234,',
    '                           1.1 * raysSpeed);',
    '',
    '  fragColor = rays1 * 0.5 + rays2 * 0.4;',
    '',
    '  if (noiseAmount > 0.0) {',
    '    float n = noise(coord * 0.01 + iTime * 0.1);',
    '    fragColor.rgb *= (1.0 - noiseAmount + noiseAmount * n);',
    '  }',
    '',
    '  float brightness = 1.0 - (coord.y / iResolution.y);',
    '  fragColor.x *= 0.1 + brightness * 0.8;',
    '  fragColor.y *= 0.3 + brightness * 0.6;',
    '  fragColor.z *= 0.5 + brightness * 0.5;',
    '',
    '  if (saturation != 1.0) {',
    '    float gray = dot(fragColor.rgb, vec3(0.299, 0.587, 0.114));',
    '    fragColor.rgb = mix(vec3(gray), fragColor.rgb, saturation);',
    '  }',
    '',
    '  fragColor.rgb *= raysColor;',
    '}',
    '',
    'void main() {',
    '  vec4 color;',
    '  mainImage(color, gl_FragCoord.xy);',
    '  gl_FragColor = color;',
    '}'
  ].join('\n');

  function createShader(gl, type, source) {
    var shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      if (window.console && console.error) {
        console.error('LightRays shader error: ' + gl.getShaderInfoLog(shader));
      }
      gl.deleteShader(shader);
      return null;
    }
    return shader;
  }

  function init() {
    var container = document.getElementById('light-rays-bg');
    if (!container) return;

    var canvas = document.createElement('canvas');
    canvas.style.cssText = 'width:100%;height:100%;display:block;';
    container.appendChild(canvas);

    var gl = canvas.getContext('webgl', { alpha: true, premultipliedAlpha: true });

    if (!gl) {
      container.parentNode.removeChild(container);
      return;
    }

    gl.clearColor(0, 0, 0, 0);

    var positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);

    var vertexShaderObj = createShader(gl, gl.VERTEX_SHADER, vertexShader);
    var fragmentShaderObj = createShader(gl, gl.FRAGMENT_SHADER, fragmentShader);
    if (!vertexShaderObj || !fragmentShaderObj) {
      container.parentNode.removeChild(container);
      return;
    }

    var program = gl.createProgram();
    gl.attachShader(program, vertexShaderObj);
    gl.attachShader(program, fragmentShaderObj);
    gl.linkProgram(program);

    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      if (window.console && console.error) {
        console.error('LightRays program error: ' + gl.getProgramInfoLog(program));
      }
      container.parentNode.removeChild(container);
      return;
    }

    gl.useProgram(program);

    var locPosition = gl.getAttribLocation(program, 'position');
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.enableVertexAttribArray(locPosition);
    gl.vertexAttribPointer(locPosition, 2, gl.FLOAT, false, 0, 0);

    var uniforms = {};
    var names = [
      'iTime', 'iResolution',
      'rayPos', 'rayDir',
      'raysColor', 'raysSpeed', 'lightSpread', 'rayLength', 'pulsating',
      'fadeDistance', 'saturation', 'mousePos', 'mouseInfluence',
      'noiseAmount', 'distortion'
    ];
    for (var n = 0; n < names.length; n++) {
      uniforms[names[n]] = gl.getUniformLocation(program, names[n]);
    }

    gl.uniform3fv(uniforms.raysColor, new Float32Array(hexToRgb(config.raysColor)));
    gl.uniform1f(uniforms.raysSpeed, config.raysSpeed);
    gl.uniform1f(uniforms.lightSpread, config.lightSpread);
    gl.uniform1f(uniforms.rayLength, config.rayLength);
    gl.uniform1f(uniforms.pulsating, config.pulsating ? 1.0 : 0.0);
    gl.uniform1f(uniforms.fadeDistance, config.fadeDistance);
    gl.uniform1f(uniforms.saturation, config.saturation);
    gl.uniform1f(uniforms.mouseInfluence, config.mouseInfluence);
    gl.uniform1f(uniforms.noiseAmount, config.noiseAmount);
    gl.uniform1f(uniforms.distortion, config.distortion);
    gl.uniform2f(uniforms.mousePos, 0.5, 0.5);

    function updatePlacement() {
      var wCSS = container.offsetWidth || window.innerWidth;
      var hCSS = container.offsetHeight || window.innerHeight;
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = Math.round(wCSS * dpr);
      var h = Math.round(hCSS * dpr);
      canvas.width = w;
      canvas.height = h;
      canvas.style.width = wCSS + 'px';
      canvas.style.height = hCSS + 'px';
      gl.viewport(0, 0, w, h);
      gl.uniform2f(uniforms.iResolution, w, h);

      var placement = getAnchorAndDir(config.raysOrigin, w, h);
      gl.uniform2f(uniforms.rayPos, placement.anchor[0], placement.anchor[1]);
      gl.uniform2f(uniforms.rayDir, placement.dir[0], placement.dir[1]);
    }

    window.addEventListener('resize', updatePlacement);
    updatePlacement();

    var mouse = { x: 0.5, y: 0.5 };
    var smoothMouse = { x: 0.5, y: 0.5 };
    var followActive = config.followMouse && config.mouseInfluence > 0;

    function onMouseMove(e) {
      var rect = container.getBoundingClientRect();
      mouse.x = (e.clientX - rect.left) / rect.width;
      mouse.y = (e.clientY - rect.top) / rect.height;
    }

    if (followActive) {
      window.addEventListener('mousemove', onMouseMove);
    }

    var animationFrameId;
    var t0 = performance.now();

    function update(time) {
      animationFrameId = requestAnimationFrame(update);
      var t = (time - t0) * 0.001;

      gl.uniform1f(uniforms.iTime, t);

      if (followActive) {
        var smoothing = 0.92;
        smoothMouse.x = smoothMouse.x * smoothing + mouse.x * (1 - smoothing);
        smoothMouse.y = smoothMouse.y * smoothing + mouse.y * (1 - smoothing);
        gl.uniform2f(uniforms.mousePos, smoothMouse.x, smoothMouse.y);
      }

      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }

    animationFrameId = requestAnimationFrame(update);

    window.addEventListener('beforeunload', function cleanup() {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', updatePlacement);
      if (followActive) window.removeEventListener('mousemove', onMouseMove);
      if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
      var ext = gl.getExtension('WEBGL_lose_context');
      if (ext) ext.loseContext();
    });
  }

  init();
})();
